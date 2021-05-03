// var path = require('path');
var gulp = require('gulp');
// var watch = require('gulp-watch');
// var sourcemaps = require('gulp-sourcemaps');
// var concat = require('gulp-concat');
// var uglify = require('gulp-uglify');
// var notify = require('gulp-notify');
// var sass = require('gulp-sass');
// var rename = require("gulp-rename");
// var browserify = require('gulp-browserify');
// var autoprefixer = require('gulp-autoprefixer');
var http = require('http');
var ecstatic = require('ecstatic');
// var html2js = require('gulp-html2js');
// var eslint = require('gulp-eslint');
// var eslint = require('gulp-eslint');
// var cssToJs = require('gulp-css-to-js');
// var merge = require('gulp-merge');


gulp.task('default', ['lint'], function () {
    http.createServer(
        ecstatic({ 
          root: __dirname,
        //   headers: {"Set-Cookie":"sessionId=38afes7a8"}
        })
    ).listen(3000);

    console.log('Listening on :3000');
});
