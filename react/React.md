# React

### react项目创建方法

```shell
$npx create-react-app test
```

[react官网地址](https://reactjs.org/)

### react运行测试命令

```shell
$yarn strat
$yarn build
$yarn test
```

### index.js格式标准

`index.js`文件是`react`的入口文件，需要导入两个重要的模块`react`、`react-dom`

```javascript
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

ReactDOM.render(
    <React.StrictMode>
    <App />
    </React.StrictMode>,
    document.querySelector('#root')
)
```

### react创建组件的方式

+ 函数方法创建组件

```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
//箭头函数创建组件
const Hello = () => <div>这是我的第一个函数组件</div>
```

+ 类组件创建方法

```javascript
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
export default Welcome;
```

+ 组合组件

```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}
```

### react事件处理

```javascript
 class App extends React.Component {
   // 事件处理程序
   handleClick() {
   console.log('单击事件触发了')
   }
   render() {
     return (
       <button onClick={this.handleClick}>点我，点我</button>
     )
   }
 }

// 通过函数组件绑定事件：
function App() {
  // 事件处理程序
  function handleClick() {
    console.log('函数组件中的事件绑定，事件触发了')
  }

  return (
    <button onClick={handleClick}>点我</button>
  )
}
```

### 从JSX中抽离事件处理程序

```javascript
class App extends React.Component {
  state = {
    count: 0
  }
  // 事件处理程序
  onIncrement() {
    console.log('事件处理程序中的this：', this)
    this.setState({
      count: this.state.count + 1
    })
  }

  render() {
    return (
      <div>
        <h1>计数器：{ this.state.count }</h1>
        <button onClick={this.onIncrement}>+1</button>
        {/* <button onClick={() => {
          this.setState({
            count: this.state.count + 1
          })
        }}>+1</button> */}
      </div>
    )
  }
```



### Component组件化

`react`是以组件化来构建页面元素的，比如`Button`、`sidebar`、`header`、`root`

创建组件的时候需要导入`React`,并且从`react`中剪构出`Component`导入`css`文件，用`class`方法继承`Component`,然后用`render(){return[html......]}`,最后导出模块`export default App`

```javascript
import React, {Component} from 'react'
import './Navstyle.css'
class Nav extends Component {
    render(){
        return<div className='nav'>
            <ul>
                <li>Home</li>
                <li>About</li>
                <li>presale</li>
                <li>11123</li>
                <li>11123</li>
            </ul>
        </div>
    }
}

export default Nav;

```

 `Navstyle.css`的样式如下：

```css
*{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

.nav{
    position: fixed;
    width: 100%;
    height: 120px;
    background-color: violet;
}
li{
    display: inline-block;
    width: 160px;
    height: 80px;
    line-height: 80px;
    background-color: thistle;
    text-align: center;
    margin: 20px;
    list-style: none;
}

```

### react属性props传参

+ props的基本使用

```javascript
// 2 接收数据
class Hello extends React.Component {
  render() {
    // console.log(this.props)
    return (
      <div>
        <h1>props: {this.props.age}</h1>
      </div>
    )
  }
}

// 1 传递数据
ReactDOM.render(<Hello name="rose" age={19} />, document.getElementById('root'))

```

+ props的特点

```javascript
class Hello extends React.Component {
  // 推荐使用props作为constructor的参数！！
  constructor(props) {
    super(props)
    // console.log(this.props)
    console.log(props)
  }

  render() {
    console.log('render：', this.props)
    return (
      <div>
        <h1>props：</h1>
      </div>
    )
  }
}
//函数组件props方式
const Hello = props => {
  console.log('props：', props)
  props.fn()
  // 修改props的值：错误演示！！！
  // props.name = 'tom'
  return (
    <div>
      <h1>props：</h1>
      {props.tag}
    </div>
  )
}

ReactDOM.render(
  <Hello
    name="rose"
    age={19}
    colors={['red', 'green', 'blue']}
    fn={() => console.log('这是一个函数')}
    tag={<p>这是一个p标签</p>}
  />,
  document.getElementById('root
```

+ props父到子通讯

```javascript
//父组件
class Parent extends React.Component {
  state = {
    lastName: '王'
  }

  render() {
    return (
      <div className="parent">
        父组件：
        <Child name={this.state.lastName} />
      </div>
    )
  }
}

// 子组件
const Child = props => {
  console.log('子组件：', props)
  return (
    <div className="child">
      <p>子组件，接收到父组件的数据：{props.name}</p>
    </div>
  )
}

ReactDOM.render(<Parent />, document.getElementById('root'))
```

+ props子到父通讯

```javascript
// 父组件
class Parent extends React.Component {
  state = {
    parentMsg: ''
  }

  // 提供回调函数，用来接收数据
  getChildMsg = data => {
    console.log('接收到子组件中传递过来的数据：', data)

    this.setState({
      parentMsg: data
    })
  }

  render() {
    return (
      <div className="parent">
        父组件：{this.state.parentMsg}
        <Child getMsg={this.getChildMsg} />
      </div>
    )
  }
}

// 子组件
class Child extends React.Component {
  state = {
    msg: '刷抖音'
  }

  handleClick = () => {
    // 子组件调用父组件中传递过来的回调函数
    this.props.getMsg(this.state.msg)
  }

  render() {
    return (
      <div className="child">
        子组件：{' '}
        <button onClick={this.handleClick}>点我，给父组件传递数据</button>
      </div>
    )
  }
}

ReactDOM.render(<Parent />, document.getElementById('root'))
```

+ props兄弟组件之间的通讯

```javascript
/* 
  兄弟组件通讯
*/

// 父组件
class Counter extends React.Component {
  // 提供共享状态
  state = {
    count: 0
  }

  // 提供修改状态的方法
  onIncrement = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  render() {
    return (
      <div>
        <Child1 count={this.state.count} />
        <Child2 onIncrement={this.onIncrement} />
      </div>
    )
  }
}

const Child1 = props => {
  return <h1>计数器：{props.count}</h1>
}

const Child2 = props => {
  return <button onClick={() => props.onIncrement()}>+1</button>
}

ReactDOM.render(<Counter />, document.getElementById('root'))
```



### react状态state和setState

+ state

```javascript
class App extends React.Component {
   // 初始化state
    constructor() {
    super()
    this.state = {
      count: 0
    }
  } 

  // 简化语法初始化state（推荐）
  state = {
    count: 10
  }

  render() {
    return (
      <div>
        <h1>计数器：{ this.state.count }</h1>
      </div>
    )
  }
}
```

+ setState

```javascript
class App extends React.Component {
  state = {
    count: 0,
    test: 'a'
  }

  render() {
    return (
      <div>
        <h1>计数器：{ this.state.count }</h1>
        <button onClick={() => {
          this.setState({
            count: this.state.count + 1
          })
        }}>+1</button>
      </div>
    )
  }
}
```

### 组件的生命周期

![组件的生命周期示意图](C:\Users\86158\Desktop\code\React\react组件生命周期.png)

+ 创建时

```javascript
class App extends React.Component {
  constructor(props) {
    super(props)

    // 初始化state
    this.state = {
      count: 0
    }
    // 处理this指向问题

    console.warn('生命周期钩子函数： constructor')
  }

  // 1 进行DOM操作
  // 2 发送ajax请求，获取远程数据
  componentDidMount() {
    // axios.get('http://api.....')

    // const title = document.getElementById('title')
    // console.log(title)
    console.warn('生命周期钩子函数： componentDidMount')
  }

  render() {
    // 错误演示！！！ 不要在render中调用setState()
    // this.setState({
    //   count: 1
    // })
    console.warn('生命周期钩子函数： render')

    return (
      <div>
        <h1 id="title">统计豆豆被打的次数：</h1>
        <button id="btn">打豆豆</button>
      </div>
    )
  }
}
```

+ 更新时

```javascript
class App extends React.Component {
  constructor(props) {
    super(props)

    // 初始化state
    this.state = {
      count: 0
    }
  }

  // 打豆豆
  handleClick = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  render() {
    return (
      <div>
        <Counter count={this.state.count} />
        <button onClick={this.handleClick}>打豆豆</button>
      </div>
    )
  }
}

class Counter extends React.Component {
  render() {
    console.warn('--子组件--生命周期钩子函数： render')
    return <h1 id="title">统计豆豆被打的次数：{this.props.count}</h1>
  }

  // 注意：如果要调用 setState() 更新状态，必须要放在一个 if 条件中
  // 因为：如果直接调用 setState() 更新状态，也会导致递归更新！！！
  componentDidUpdate(prevProps) {
    console.warn('--子组件--生命周期钩子函数： componentDidUpdate')

    // 正确做法：
    // 做法：比较更新前后的props是否相同，来决定是否重新渲染组件
    console.log('上一次的props：', prevProps, ', 当前的props：', this.props)
    if (prevProps.count !== this.props.count) {
      // this.setState({})
      // 发送ajax请求的代码
    }

    // 错误演示！！！
    // this.setState({})

    // 获取DOM
    // const title = document.getElementById('title')
    // console.log(title.innerHTML)
  }
}
```

+ 卸载时

```javascript
class App extends React.Component {
  constructor(props) {
    super(props)

    // 初始化state
    this.state = {
      count: 0
    }
  }

  // 打豆豆
  handleClick = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  render() {
    return (
      <div>
        {this.state.count > 3 ? (
          <p>豆豆被打死了~</p>
        ) : (
          <Counter count={this.state.count} />
        )}
        <button onClick={this.handleClick}>打豆豆</button>
      </div>
    )
  }
}

class Counter extends React.Component {
  componentDidMount() {
    // 开启定时器
    this.timerId = setInterval(() => {
      console.log('定时器正在执行~')
    }, 500)
  }

  render() {
    return <h1>统计豆豆被打的次数：{this.props.count}</h1>
  }

  componentWillUnmount() {
    console.warn('生命周期钩子函数： componentWillUnmount')

    // 清理定时器
    clearInterval(this.timerId)
  }
}
```

### 高阶组件



### react路由

首先导入路由模块

```javascript
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'
```

然后在需要路由的地方设置路由

```javascript
//App.js
import React from 'react'
import {BrowserRouter as Router, Route,Link} from 'react-router-dom'
import Home from './components/Home'

export default class App extends React.Component{
    render(){
        return(
            <Router>
            <div className='app'>
                <Route path='/' component={Home}></Route>
            </div>
            </Router>
        )
    }
}
```

```javascript
//Home.js
import React from 'react'
import {BrowserRouter as Router, Route,Link} from 'react-router-dom'
import Nav from './Nav'
import Content from './Content'

export default class Home extends React.Component{
    render(){
        return(
            <Router>
            <div className='home'>
                <Route component={Nav}></Route>
                <Route component={Content}></Route>
            </div>
            </Router>
        )
    }
}
```



