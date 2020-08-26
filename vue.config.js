module.exports = {
    runtimeCompiler: true,
    publicPath: process.env.NODE_ENV === 'production' ? 'public' : '/',
    pages: {
        index: {
            entry: 'src/main.js',
            template: 'public/index.html',
            filename: 'index.html'
        }
    }
}