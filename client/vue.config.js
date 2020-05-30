const path = require("path");

module.exports = {
  outputDir: path.resolve(__dirname, "../server/dist/static"),
  assetsDir: ".",
  indexPath: "../index.html",
  publicPath: "/static",
};
