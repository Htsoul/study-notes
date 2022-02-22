## `JSON`知识点

### `JSON`语法

- 名称/值由字段名称构成，后跟冒号和值

> "name" : "Bill Gates"

- `JSON`与`JavaScript`的比较
- `JSON`

> ```json
> {"name" : "BILL"}
> ```

- ​		`JavaScript`

> ```javascript
> {name : "BILL"}
> ```

- 因为` JSON` 语法由` JavaScript` 对象标记法衍生而来能够像这样访问` JavaScript` 对象

> ```javascript
> var person =  { name : "Bill Gates", age : 62, city : "Seattle" }  //实例
> console.log(person.name)  //控制台输出结果为 Bill Gates
> console.log(person["name"])  //控制台输出结果为 Bill Gates
> ```

- 在` JSON` 中，值(右边的值)必须是以下数据类型之一
  - 字符串
  - 数字
  - 对象（`JSON`对象）
  - 数组
  - 布尔
  - Null
- `JSON` 的值*不可以* 是以下数据类型之一 
  - 函数
  - 日期 **(需要包含日期请写为字符串)**
  - undefined

- 最简单的`JSON`示例

> ```json
> {
>     "name": "周大大",
>     "age": 18,
>     "sex": "男"
> }
> ```

- 稍微复杂一点的`JSON`示例

> ```json
> {
>     "admin":{
>         "name": "admin",
>         "passwad": 123456
>     },
>     
>     "users":[{
>         "name": "周大",
>         "passwad": 158862
>     },
>           {
>         "name": "孔明",
>         "passwad": 125582
>     },
>           {
>         "name": "庞统",
>         "passwad": 112233
>     }]
> }
> ```

- 嵌套的	`JSON`  对象或者说一个` JSON` 对象中的值可以是另一个` JSON `对象

> ```javascript
> myObj =  {
>    "name":"Bill Gates",
>    "age":62,
>    "cars": {
> 	  "car1":"Porsche",
> 	  "car2":"BMW",
> 	  "car3":"Volvo"
>    }
> }
> //能够通过使用点号和括号访问嵌套的 JSON 对象
> var x = myObj.cars.car2
> var y = myObj.cars["car3"]
> //删除对象属性
> delete myObj.cars.car2
> delete myObj.cars["car3"]
> ```

- `JavaScript` 提供內建函数把以` JSON` 格式写的字符串转换为原生 JavaScript 对象

```javascript
Json.parse()
```

- `JSON.parse() `函数的第二个参数被称为 **reviver**, 将字符串转换为日期，使用 **reviver **函数

> ```javascript
> var text =  '{ "name":"Bill Gates", "birth":"1955-10-28", "city":"Seattle"}'
> var obj = JSON.parse(text, function (key, value) {
>     if  (key == "birth") {
>         return new Date(value)
>     } else {
>          return value
>    }})
> ```

-  `JavaScript `函数` JSON.stringify()` 将它转换为字符串

```javascript
JSON.stringify()
```

- **注意：**`JSON `的常规用途是同 web 服务器进行数据传输。在从 web 服务器接收数据时，数据永远是字符串通过 `JSON.parse()` 解析数据，这些数据会成为 `JavaScript `对象

> ```javascript
> var oReq = new XMLHttpRequest()
> oReq.onload = function(e) {
>   var arraybuffer = oReq.response; // 不是 responseText ！
>   /* ... */
> }
> oReq.open("GET", url)
> oReq.responseType = "arraybuffer"
> oReq.send()
> ```

- 能够通过使用 `for-in `遍历对象属性

> ```javascript
> var myObj =  { "name":"Bill Gates", "age":62, "car":null }
> for (var x in myObj) {
>    x = myobj
> }
> console.log(x)
> ```

- `JSO`对象中的嵌套数组，数组中的值也可以另一个数组，或者甚至另一个 `JSON` 对象

> ```javascript
> var myObj =  {
>    "name":"Bill Gates",
>    "age":62,
>    "cars": [
> 	  { "name":"Porsche",  "models":[ "911", "Taycan" ] },
> 	  { "name":"BMW", "models":[ "M5", "M3", "X5" ] },
> 	  { "name":"Volvo", "models":[ "XC60", "V60" ] }
>    ]
> }
> //使用索引号来修改数组
> myObj.cars[0] 
> ```

**注意：**`JSON	`文件的内容格式为字符串，导出来用的话要使用`JSON.parse()`方法转变成对象使用

如果涉及到`JSON`文件的修改需要使用`JSON.stringify()`方法把对象转变字符串重新写入到`JSON`文件中	