/*!
 * 'grunt' alone creates a new, completed images directory
 * 'grunt clean' removes the images directory
 * 'grunt responsive_images' re-processes images without removing the old ones
 */
'use strict'

var ngrok = require('grunt-ngrok');

module.exports = function(grunt) {

  // Load grunt tasks
  require('load-grunt-tasks')(grunt);

  // Grunt configuration
  grunt.initConfig({
    responsive_images: {
      dev: {
        options: {
          engine: 'im',
          sizes: [
            {
              name: '',
              suffix: '_1x',
              width: 800,
              quality: 60
            },
            {
              name: '',
              suffix: '_2x',
              width: 1600,
              quality: 60
            },
            {
              name: '',
              suffix: '_1x',
              width: 640,
              quality: 60
            },
            {
              name: '',
              suffix: '_2x',
              width: 1280,
              quality: 60
            }
          ]
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
          create: ['prod/images/', 'prod/fonts/']
        },
      },
    },

    // Copy the 'fixed' images that don't go through processing into the images/directory
    // copy_imgs: {
    //   dev: {
    //     files: [{
    //       expand: true,
    //       cwd: 'src/images/fixed/',
    //       src: '*.{gif,jpg,png}',
    //       dest: 'prod/images/fixed/',
    //       flatten: true,
    //       filter: 'isFile'
    //     }]
    //   },
    // },

    copy: {
      dev: {
        files: [{
          expand: true,
          cwd: 'src/fonts/',
          src: '*.{eot,svg,ttf,woff}',
          dest: 'prod/fonts/',
          flatten: true,
          filter: 'isFile'
        }]
      },
    },

    // BrowserSync Serve
    browserSync: {
      bsFiles: {
          src: ['/prod/css/main.css', '/prod/index.html']
      },
      options: {
          server: {
            baseDir: './prod/'
          }
      }
    },
   
   });
  
  grunt.registerTask('default', ['clean', 'mkdir', 'copy', 'responsive_images', 'browserSync']);
};