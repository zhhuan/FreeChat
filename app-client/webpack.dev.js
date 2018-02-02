const path = require('path');

module.exports = {
	entry: './src/main.js',
	output: {
		filename: 'bundle.js',
		path: path.resolve(__dirname,'dist'),
		publicPath: 'http://localhost:8088/js'
	},
	module: {
		rules: [
			{ 
			  test: /\.vue$/, 
			  use: [ 
				'vue-loader'
			  ]
			},
			{ 
			  test: /\.js$/, 
			  use: [
			    'babel-loader'
			  ],
			  exclude: /node_modules/
			},
			{ 
			  test: /\.css$/, 
			  use: [
			  	'vue-style-loader',
			  	'css-loader'
			  ]
			},
			{ 
			  test: /\.sass$/, 
			  use: [
			  	'vue-style-loader',
			  	'css-loader',
			  	'sass-loader'
			  ]
			},
			{ 
			  test: /\.(png|svg|jpe?g|gif)$/, 
			  use: [
			    {
			      loader: 'url-loader',
			      options: {
			      	limit: 8192,
			      	name: 'images/[name].[ext]'
			      }
			    }
			  ]
			}
		]
	},
	devServer: {
		host: '0.0.0.0',
		contentBase: path.resolve(__dirname, 'dist'),
		port: 8088
	},
	devtool: 'inline-source-map'
};