#SublimeConcat

Automatically concatenate all of the dependencies in the current file

## Usage:

Define the dependencies using the @import syntax

CSS:
    
        @import url('bootstrap.min.css');
    
        body { background-color: #fff; }

JS:
    
        //@import url('jquery.min.js'); 
    
        $(document).ready(function(){
            console.log('ready');
        });

`Command + Shift + C` will concatenate all of the dependences into a new file: `{{filename}}.cat.{{extension}}`

Use with [YUI Compressor](https://github.com/leon/YUI-Compressor) and [SublimeOnSaveBuild](https://github.com/alexnj/SublimeOnSaveBuild) for automatic concat and minify