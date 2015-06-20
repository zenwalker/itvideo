var gulp = require('gulp')
  , stylus = require('gulp-stylus')
  , concat = require('gulp-concat')
  , postcss = require('gulp-postcss')
  , rebaseUrls = require('gulp-css-rebase-urls')
  , autoprefixer = require('autoprefixer');


/**
 * Config
 */

var sources = {
  app: {
    css: [
      './static_src/components/*.styl'
    ]
  }
};

var config = {
  root: './static'
};


/**
 * Tasks
 */

gulp.task('css', function() {
  var processors = [
    autoprefixer(config.prefixer)
  ];
  gulp.src(sources.app.css)
    .pipe(stylus(config.stylus))
    .pipe(rebaseUrls(config.rebaseUrls))
    .pipe(concat('app.css'))
    .pipe(postcss(processors))
    .pipe(gulp.dest('./static'));
});
