    
    Disclaimer:

	The compressed versions of Prototype/Scriptaculous included in this package are 
	NOT SUPPORTED by the Prototype Development Team or Thomas Fuchs. If you find a bug,
	please email at john.david.dalton@gmail.com.
    
    
    Instructions:
	
	* This pack contains the following compressed versions of Prototype: 1.4, 1.5, 1.5.1.1
	  and Scriptaculous: 1.7.1_beta3
	
	* The root folder has an example using one of the smallest Prototype 1.5.1 forms in this package.
	
	* prototype.js is prototype-1.5.1.1-shrinkvars.js.
	
	* "Protoculous" is a single file with Prototype and Scriptaculous combined.
	
	
	Open the "files" folder.
	Choose either 'original', 'formatted', or 'compressed'.
	
	Original   > The original unmodified forms of all the Prototype/Scriptaculous versions.
	
	Formatted  > The formatted forms of all the Prototype/Scriptaculous versions.
		     These versions contain all the semicolons, regExp mods and such that make them work with the compressors.
	
	Compressed > The compressed forms of all the Prototype/Scriptaculous versions.
		     Each version has 2 different compressed forms.
			
			- packer: compressed with Dean Edward's Packer 3 \w "Base62 encode" and "Shrink variables" options
			- shrinkvars : compressed with Dean Edward's Packer 3 \w "Shrink variables" option only
	
	Gzipped    > The "gzipped" folders contain the gzipped forms of all the scripts in the current folder.
	
	
	Realistically, I would stick to the gzipped “shrinkvars” versions.
	They have no js compression, which means no startup delay.
	They are also the smallest file size (Prototype 1.5.1.1 is 15.8kb).
	To load gzipped files you need to go through a server side language such as PHP.
	Some have used the .gz file directly but that’s not universally supported.
	
	* Learn about Real File Compression at: 
	* http://www.thinkvitamin.com/features/webapps/serving-javascript-fast
	*
	* OR JavaScript/CSS file concatenation and compression at:
	* http://code.google.com/p/minify/
	* http://rakaz.nl/item/make_your_pages_load_faster_by_combining_and_compressing_javascript_and_css_files
	*
	* OR Prado - The awesome PHP Framework that utilize script concatenation and compression at:
	* http://www.pradosoft.com
	* http://www.pradosoft.com/demos/quickstart/?page=Advanced.Scripts3
	*
	* OR Andrea Giammarchi has created a great GzOutput.class for PHP 5.
	* Use in conjunction with the "shrinkvars" js versions to get the best of the gzipped goodness.
	* http://www.devpro.it/php5_id_145.html
	* http://webreflection.blogspot.com/
	
	
	Example Prototype usage:
	    
	    Good:
	    <script type="text/javascript" src="prototype.js"></script>
	    
	    Good:
	    <script type="text/javascript" src="gz.php?src=prototype"></script>
	    
	    Bad:
	    <script type="text/javascript" src="prototype.gz"></script>
	
	Example Protoculous usage:
	    
	    Good:
	    <script type="text/javascript" src="protoculous.js"></script>
	    
	    Good:
	    <script type="text/javascript" src="protoculous-packer.js"></script>
	    
	    Good:
	    <script type="text/javascript" src="protoculous.js?load=addon"></script>
	    
	    Good:
	    <script type="text/javascript" src="gz.php?src=protoculous"></script>

	    Bad:
	    <script type="text/javascript" src="prototype.gz"></script>
    
    
    Tested successfully on:
	
	win: 
	    opera 9.10
	    firefox 2.0.0.1
	    ie 7.0
	    ie 6.0.2
	    ie 5.5
	    safari 3 (xp beta)
	    
	mac :
	    firefox 1.5.01
	    firefox 2.0.0.2
	    camino 1.0.4
	    opera 9.1
	    omniWeb 5.1.3
	    safari 1.3.2
	    safari 2.0.2
	    safari 2.0.4
	    safari 3 (osx 10.4.9 beta)
	    webkit 2.0.4 (nightly build)
	    omniweb 5.5.4
	    
    
    
    Tested unsuccessfully on:
	
	win: 
	    ie 5.1
	
	mac :
	    ie 5.2
	    opera 6.3
    
    
    Interesting note:
	
	Safari doesn’t like Dean Edward's “Packer 2” when it removes the semicolons after a “throw”.
	I had to add those back to all the encodings.
	
	Safari 2.0.4/Omniweb 5.5.4 have a bug in them that causes certian "High ASCII" text in eval()'s to error out.
	For example: eval('if(/"/.¡(""));'.replace(/¡/g,'test'));
	
	That is why I switched to none High ASCII compressions.
    
    
    Other/Thanks:
	
	Thomas : http://protoculous.wikeo.be/
	Thanks to Thomas for inspiring me to produce my own "Protoculous".
	
	Dean Edwards Packer : http://dean.edwards.name/packer/
    	Thanks to Dean Edwards, Thomas Fuchs, Sam Stephenson, the Prototype Dev Team, and others who have helped me.
    
    
    History:
	
	v2.16b - Fixed Protoculous's missing require() and load() methods.

	v2.16 - removed "bragging rights" files (they seemed to distract)
		added support for Prototype 1.5.2_pre0 and Scriptaculous 1.7.1_beta3_rev7191
		the formatted Prototype 1.5.2_pre0 contains additional fixes for the following tickets:
		    http://dev.rubyonrails.org/ticket/8851
		    http://dev.rubyonrails.org/ticket/8843

	v2.15 - updated Prototype to 1.5.1.1
		confirmed safari 3 support
	
	v2.14 - added support for Scriptaculous 1.7.1_beta3
		added more links to info on JavaScript concatenation and compression
	
	v2.13 - added Scriptaculous 1.7.1_beta2 and Protoculous (1.5.1 + 1.7.1_beta2)
		used new compressor in the bragging files (http://www.bananascript.com/) //wtf is with that name choice?!?!
		removed support for MooTool's Prototype lite.
		added new tool to format the massive Scriptaculous code.
		organized the links a bit
	
	v2.12 - added Prototype 1.5.1 (final)
	
	v2.11 - added Prototype 1.5.1rc4
	
	v2.10 - removed memtronics, ultra, and custom compressed versions (they were just proofs of concept)
		compressed files using Dean Edwards Packer 3
		moved away from the letter versioning for numbers
		added Prototype 1.5.1rc3	
	
	v2.0d - name changed to "protopacked".
		added support for safari 2.0.0.4 and variants
		confirmed ie 7 support
		confirmed camino support
		added link to Andrea Giammarchi's GzOutput.class for PHP 5
	
	v2.0c - added Prototype 1.5.1rc2 to the package.
		added link to WinMerge (used to quickly format new releases)
	
	v2.0b - fixed issues with Safari and added a "no white-space" version for each.
	
	v2.0a - removed the charset "iso-8859-1" from the examples and remove the emphasis on it.
	
	v2.0  - added dean edwards packer to the compressed files.
		added more links
	
	v1.0  - initial release

