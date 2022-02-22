#  Webpack笔记

### 什么是webpack

[webpack官网](https://webpack.docschina.org/)

webpack是模板打包工具，WebPack也可以看做是**模块打包机**：它做的事情是，分析你的项目结构，找到JavaScript模块以及其它的一些浏览器不能直接运行的拓展语言（Scss，TypeScript等），并将其打包为合适的格式以供浏览器使用。

### webpack怎么使用？

```shell
npm i webpack -g  //全局安装webpack
```

使用的话就直接在终端输入以下代码

```shell
webpack  //输入webpack命令即可调用webpack打包
```

### webpack的标准化文件格式

+ `dist`  //打包之后的产品放置目录一般有`build.js`
+ `node_modules`  //下载的依赖包存放目录
+ `src`  //静态资源存放目录
  - `css`  //css文件存放目录
  - `js`  //js文件存放目录
  - `fonts`  //字体图标存放目录，比如阿里的`iconfont`，文件格式有`.ttf`,`.svg`
  - `images`  //图片存放目录，一般有`jpg`,`png`,`svg`,`jif`等
  - `index.js`  //一般是入口文件，原来是`main.js`
  - `index.html`  //入口页面
+ `webpack-config.js` //webpack的配置文件（自己创建）
+ `package-json`  //通过`npm init -y`命令执行后生成的`json`文件

### webpack中webpack-config.js配置文件一般格式

```JavaScript
const { resolve } = require('path')
//需要下载该插件包
const HtmlWebpackPlugin = require('html-webpack-plugin')
//暴露模块
module.exports = {
    //入口文件
    entry: './src/index.js',
    //输出
    output: {
        //输出文件名
        filename: 'built.js',
        //输出文件路径
        path: resolve(__dirname, 'build')
    },
    //loader的配置
    module: {
        //详细loader配置
        rules: [
            {
                //匹配哪些文件
                test: /\.css$/,
                //使用哪些loader进行处理
                use: [
                    //use数组中的laoder执行顺序，从右到左，从下到上，依次执行
                    //创建style标签，将js样式资源插入进行，添加到head中生效
                    'style-loader',
                    //将css文件变成commonjs模块加载js中，里面内容是样式字符串
                    'css-loader'
                ]
            },
            {
                //匹配哪些文件
                test: /\.less$/,
                //使用多个loader用use
                //使用哪些loader进行处理
                use: [
                    //use数组中的laoder执行顺序，从右到左，从下到上，依次执行
                    //床架style标签，将js样式资源插入进行，添加到head中生效
                    'style-loader',
                    //将css文件变成commonjs模块加载js中，里面内容是样式字符串
                    'css-loader',
                    //将less文件编译成css文件
                    //需要下载less-loader和less
                    'less-loader'
                ]
            },
            {
                //处理图片资源
                //默认处理不了html中的图片资源
                test: /\.(jpg|png|gif)$/,
                //使用一个用loader
                //下载url-loader,file-loader
                loader: 'url-loader',
                options: {
                    //图片大小小于8kb就会被base64处理
                    //优点：减少请求数量，减轻服务器压力
                    //缺点：图片体积会更大，文件请求速度更慢
                    limit: 8*1024,
                    //因为url-loader默认使用的是es6中的模块化解析，而html-loader引入的是common.js
                    //解析时会出现问题
                    //解决办法：关闭url-loader中的es6模块化，使用common.js解析
                    esModule: false,
                    //给图片重命名
                    //[hash:10]取图片hash的前10位
                    //[ext]取文件原来的拓展名
                    name: '[hash:10].[ext]'
                }
            },
            {
                test: /\.html$/,
                //处理html中的img文件，负责引入img，从而能被url-loader处理
                loader: 'html-loader'
            }
        ]
    },
    plugins: [
        //plugins配置
        //html-webpack-plugin
        //功能：默认会创建一个空的html，自动引入并且打包所有的资源（js/css）
        new HtmlWebpackPlugin({
            //复刻'./src/index.html', 并自动引入并且打包所有的资源（js/css）
            template: './src/index.html',
            //压缩html文件
            minify: {
                //移除空格
                collapseWhitespace: true,
                //移除注释
                removeComments: true
            }
        })
    ],
    //模式 development生产模式，production开发模式，自动压缩js文件
    mode: 'development',
    //开发服务器，用来自动化
    devServer: {
        //运行项目目录，构建之后的项目目录
        static: resolve(__dirname, 'public/build'),
        //启用gzip压缩
        compress: true,
        //端口号
        port: 3000,
        //打开默认浏览器
        open: true,
        //热重载
        hot: true
    },
    //源码解析
   devtool: 'eval-source-map'

}
```

### ES6语法转换

由于Client浏览器端不识别ES6语法，所以需要把ES6语法降级，所以使用webpack命令降级,然后在html文件中引用build.js文件

```shell
webpack ./src/main.js ./dist/build.js
```

### webpack-dev-server的使用

由于需要经常性的修改代码查看样式，所以我们需要在本地安装一个像`nodemon`一样的自动打包并且刷新的命令，那就是`webpack-dev-server`，使用`webpack-dev-server`需要注意的是要在本地再次安装`webpack`

```shell
npm i webpack-dev-server -D  //在本地安装webpack-dev-server
```

```shell
npm i webpack -D  //在本地安装webpack
```

我们需要在`pack-json`文件中修改配置

```json
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    //配置webpack-dev-server
    //--open编译执行后自动打开默认浏览器
    //--port 3000指定打开的端口号为3000
    //指定src为项目的根路径
    //--hot热更新或者是热重载
    "dev": "webpack-dev-server --open --port 3000 --contentBase src --hot"
  }
```



