/*
 After you have changed the settings at "Your code goes here",
 run this with one of these options:
  "grunt" alone creates a new, completed images directory
  "grunt clean" removes the images directory
  "grunt responsive_images" re-processes images without removing the old ones
*/

module.exports = function(grunt) {

  grunt.initConfig({
    responsive_images: {
      dev: {
        options: {
          engine: 'im',
          sizes: [{
            name: '',
            suffix: '_large',
            width: 800,
            quality: 60
          }]
        },
        files: [{
          expand: true,
          src: ['*.{gif,jpg,png}'],
          cwd: 'src/images/',
          dest: 'prod/images/'
        }]
      }
    },

    /* Clear out the images directory if it exists */
    clean: {
      dev: {
        src: ['prod/images/'],
      },
    },

    /* Generate the images directory if it is missing */
    mkdir: {
      dev: {
        options: {
          create: ['prod/images/', 'prod/images/fixed/']
        },
      },
    },

    /* Copy the "fixed" images that don't go through processing into the images/directory */
    copy: {
      dev: {
        files: [{
          expand: true,
          cwd: 'src/images/fixed/',
          src: '*.{gif,jpg,png}',
          dest: 'prod/images/fixed/',
          flatten: true,
          filter: 'isFile'
        }]
      },
    },

    // BrowserSync Serve
    browserSync: {
      bsFiles: {
          src : ['prod/css/main.css', 'prod/index.html']
      },
      options: {
          server: {
              baseDir: "./prod/"
          }
      }
    }
  });
  
  grunt.loadNpmTasks('grunt-responsive-images');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-mkdir');
  grunt.loadNpmTasks('grunt-browser-sync');

  grunt.registerTask('default', ['clean', 'mkdir', 'copy', 'responsive_images', 'browserSync']);

};
