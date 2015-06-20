var gulp = require('gulp')
  , stylus = require('gulp-stylus')
  , concat = require('gulp-concat')
  , postcss = require('gulp-postcss')
  , rebaseUrls = require('gulp-css-rebase-urls')
  , autoprefixer = require('autoprefixer')
  , path = require('path');


/**
 * Config
 */

var sources = {
  app: {
    css: [
      './client/common/reset.styl',
      './client/components/*.styl'
    ]
  }
};

var config = {
  root: './static',
  stylus: {
    import: [
      path.join(__dirname, 'client/common/variables'),
      path.join(__dirname, 'client/common/mixins'),
      path.join(__dirname, 'client/common/colors')
    ]
  }
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
    .pipe(gulp.dest('./client/build'));
});

gulp.task('watch', function() {
  gulp.watch(sources.app.css, ['css']);
});
