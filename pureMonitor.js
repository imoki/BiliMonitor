
/*
    作者：imoki
    仓库：https://github.com/imoki
    脚本名：pureMonitor
    脚本兼容: 金山文档（airscript 1.0）
    更新时间：20241122
    简介：监控bilibili合集视频是否更新。
          纯监控脚本，仅监控合集是否更新，并不会下载视频。若需下载视频请配合downMonitor.py使用。
          将本脚本加入金山文档定时任务，设置每日或多日一次即可，若有新增合集视频则会发送消息通知。请勿频繁监控。
          填写bvidList和key，bvidList填合集的bvid，key填bark推送的key
*/

// 配置自定义
const bvidList = ["BVxxxx"];    // 需要监控的合集
const key = "xxxxxxxx"; // bark的key

// 接口
const apiInfoUrl = "https://bili.zhouql.vip/meta/";


var sheetNameConfig = "biliMonitor"; // 分配置表名称
// 表中激活的区域的行数和列数
var row = 0;
var col = 0;
var maxRow = 100; // 规定最大行
var maxCol = 26; // 规定最大列
var workbook = [] // 存储已存在表数组
var colNum = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
var messagePushHeader = "【bili监控】\n"
var message = ""

function sleep(d) {
  for (var t = Date.now(); Date.now() - t <= d; );
}

// ======================生成表修改相关开始======================
// 激活工作表函数
function ActivateSheet(sheetName) {
    let flag = 0;
    try {
      // 激活工作表
      let sheet = Application.Sheets.Item(sheetName);
      sheet.Activate();
      // console.log("🥚 激活工作表：" + sheet.Name);
      flag = 1;
    } catch {
      flag = 0;
      console.log("🍳 无法激活工作表，工作表可能不存在");
    }
    return flag;
}

// 存储已存在的表
function storeWorkbook() {
  // 工作簿（Workbook）中所有工作表（Sheet）的集合,下面两种写法是一样的
  let sheets = Application.ActiveWorkbook.Sheets
  sheets = Application.Sheets

  // 清空数组
  workbook.length = 0

  // 打印所有工作表的名称
  for (let i = 1; i <= sheets.Count; i++) {
    workbook[i - 1] = (sheets.Item(i).Name)
    // console.log(workbook[i-1])
  }
}

// 判断表是否已存在
function workbookComp(name) {
  let flag = 0;
  let length = workbook.length
  for (let i = 0; i < length; i++) {
    if (workbook[i] == name) {
      flag = 1;
      console.log("✨ " + name + "表已存在")
      break
    }
  }
  return flag
}

// 创建表，若表已存在则不创建，直接写入数据
function createSheet(name) {
  // const defaultName = Application.Sheets.DefaultNewSheetName
  // 工作表对象
  if (!workbookComp(name)) {
    Application.Sheets.Add(
      null,
      Application.ActiveSheet.Name,
      1,
      Application.Enum.XlSheetType.xlWorksheet,
      name
    )
  }
}

// 判断表格行列数，并记录目前已写入的表格行列数。目的是为了不覆盖原有数据，便于更新
function determineRowCol() {
  for (let i = 1; i < maxRow; i++) {
    let content = Application.Range("A" + i).Text
    if (content == "")  // 如果为空行，则提前结束读取
    {
      row = i - 1;  // 记录的是存在数据所在的行
      break;
    }
  }
  // 超过最大行了，认为row为0，从头开始
  let length = colNum.length
  for (let i = 1; i <= length; i++) {
    content = Application.Range(colNum[i - 1] + "1").Text
    if (content == "")  // 如果为空行，则提前结束读取
    {
      col = i - 1;  // 记录的是存在数据所在的行
      break;
    }
  }
  // 超过最大行了，认为col为0，从头开始

  // console.log("✨ 当前激活表已存在：" + row + "行，" + col + "列")
}

// 统一编辑表函数
function editConfigSheet(content) {
  determineRowCol();
  let lengthRow = content.length
  let lengthCol = content[0].length
  if (row == 0) { // 如果行数为0，认为是空表,开始写表头
    for (let i = 0; i < lengthCol; i++) {
      Application.Range(colNum[i] + 1).Value = content[0][i]
    }

    row += 1; // 让行数加1，代表写入了表头。
  }

  // 从已写入的行的后一行开始逐行写入数据
  // 先写行
  for (let i = 1 + row; i <= lengthRow; i++) {  // 从未写入区域开始写
    for (let j = 0; j < lengthCol; j++) {
      Application.Range(colNum[j] + i).Value = content[i - 1][j]
    }
  }
  // 再写列
  for (let j = col; j < lengthCol; j++) {
    for (let i = 1; i <= lengthRow; i++) {  // 从未写入区域开始写
      Application.Range(colNum[j] + i).Value = content[i - 1][j]
    }
  }
}

// ======================生成表修改相关结束======================
// 使用正则表达式匹配以'http://'或'https://'开头的字符串
function isHttpOrHttpsUrl(url) {
    // '^'表示字符串的开始，'i'表示不区分大小写
    const regex = /^(http:\/\/|https:\/\/)/i;
    // match() 方法返回一个包含匹配结果的数组，如果没有匹配项则返回 null
    return url.match(regex) !== null;
}

// 推送bark消息
function bark(message, key) {
  message = messagePushHeader + message // 消息头最前方默认存放：【xxxx】
  message = encodeURIComponent(message)
  BARK_ICON = "https://s21.ax1x.com/2024/06/23/pkrUkfe.png"
  let url = ""
  if(isHttpOrHttpsUrl(key)){  // 以http开头
    url = key + "/" + message + "/" + "?icon=" + BARK_ICON
  }else{
    url = "https://api.day.app/" + key + "/" + message + "/" + "?icon=" + BARK_ICON;
  }
  
  // 若需要修改推送的分组，则将上面一行改为如下的形式
  // let url = 'https://api.day.app/' + bark_id + "/" + message + "?group=分组名";
  let resp = HTTP.get(url, {
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
  });
  sleep(5000);
}

// 比对正确时，时间是相同
function compTimestamp(updatedTime)
{ 
  lastTime = Application.Range("A2").Text
  // console.log(lastTime)
  //  console.log(updatedTime)
  if(lastTime == updatedTime){
    // console.log("时间一致")
    return true
  }else{
    return false
  }
}


function getLatestEpisodeTime(bvid) {
  const url = apiInfoUrl + bvid;

  resp = HTTP.fetch(url, {
      method: "get",
      // headers: headers,
      // data: data
  });

  // console.log(resp)
  resp = resp.json()

  const result = [];
  if (resp.code === 0) {
      const episodes = resp.data.ugc_season.sections[0].episodes;
      const episode = episodes[episodes.length - 1];
      const title = episode.title;
      const aid = episode.aid;
      const cid = episode.cid;
      const ctime = episode.arc.ctime;
      const episodesDict = {
          title,
          aid,
          cid,
          ctime
      };
      result.push(episodesDict);
  }
  // console.log(result);
  return result;

}

function writeMessage(content) {
    console.log(content);
    message += content;
}


function formatTimestamp(timestamp) {
    const date = new Date(timestamp * 1000); // 将秒时间戳转换为毫秒时间戳
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0'); // 月份从0开始，需要加1
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}${month}${day}`;
}


// 创建配置表表
function createConfig(){
  createSheet(sheetNameConfig) // 若配置表不存在创建表

  if(ActivateSheet(sheetNameConfig)) // 激活配置表
  {

  }
}

function init(){
  createConfig()
}

function main(){

  init()

  for (const bvid of bvidList) {
    const content = `🎮️ 监控 ${bvid}\n`;
    writeMessage(content);

    const result = getLatestEpisodeTime(bvid);
    sleep(3000)

    if (result.length !== 0) {
        for (const item of result) {
            const cid = item.cid;
            const ctime = item.ctime;
            const content = `🧸 最新集CID: ${cid}\n`;
            writeMessage(content);

            // 写入时间戳
            if(compTimestamp(ctime) == false){
              // 不同则更新最新时间和脚本
              Application.Range("A2").Value = ctime

              // 将ctime时间戳转换为20241121的格式
              const formattedCtime = formatTimestamp(parseInt(ctime));
              const content2 = `✨ 已更新最新视频，最新集时间: ${formattedCtime}\n`;
              writeMessage(content2);
              // 发送消息，通知
              bark(message, key)
              

            }else{
              console.log("✨ 已是最新集，无需更新")


            }


            
        }
    } else {
        const content = `[ - ] 最新集获取失败\n`;
        writeMessage(content);
        // 发送消息，通知
        bark(message, key)
    }


  }




}

main()

