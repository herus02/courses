/*
 * Arquivo utilizado na aula de compressão, otimização e automação
 * Lesson 2 - Units, Formats, Environments
 *
 */

module.exports = function(grunt) {

  grunt.initConfig({
    responsive_images: {
      dev: {
        options: {
          engine: 'im',
          sizes: [{
            name: 'small',
            width: '30%',
            suffix: '_small',
            quality: 20
          },{
            name: 'large',
            width: '50%',
            suffix: '_large',
            quality: 40
          }]
        },
        files: [{
          expand: true,
          src: ['*.{gif,jpg,png}'],
          cwd: 'images/',
          dest: 'images/'
        }]
      }
    },
  });

  grunt.loadNpmTasks('grunt-responsive-images');
  grunt.registerTask('default', ['responsive_images']);

};
