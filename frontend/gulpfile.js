var gulp = require('gulp'),
    connect = require('gulp-connect');

gulp.task('connect', function() {
    connect.server({
        port: 8081,
        root: '.',
        livereload: true
    });
});

gulp.task('html', function () {
    gulp.src('*.html')
    .pipe(connect.reload());
});

gulp.task('watch', function () {
  gulp.watch(['*.html'], ['html']);
  gulp.watch(['js/*.*'], ['html']);
});

gulp.task('default', ['connect', 'watch']);