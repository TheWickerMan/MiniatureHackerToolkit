To quickly display the version of the library in use - enter the following into the browser console:

# Check all of the below libraries

```
async function DependencyChecker(){;
var JSDependencies=[];
try{JSDependencies.push("JQuery Version: "+jQuery().jquery)};
catch(e){};
try{JSDependencies.push("JQuery-UI Version:"+jQuery.ui.version)};
catch(e){};
try{JSDependencies.push("Knockout Version: "+ko.version)};
catch(e){};
try{JSDependencies.push("Bootstrap Version: "+$.fn.tooltip.Constructor.VERSION)};
catch(e){};
try{JSDependencies.push("Angular Version: "+angular.version.full)};
catch(e){};
try{JSDependencies.push("Vue Version: "+Vue.version)};
catch(e){};
if(JSDependencies.length>0){alert(JSDependencies.join("\n"))};
};
DependencyChecker();
```

# JQuery


```jQuery().jquery``` or ```alert("JQuery Version: "+jQuery().jquery)```


# JQuery-UI


```jQuery.ui.version``` or ```alert("JQuery-UI Version: "+jQuery.ui.version)```


# Knockout
 

```ko.version``` or ```alert("Knockout Version: )+ko.version)```


# Bootstrap Version


```$.fn.tooltip.Constructor.VERSION``` or ```alert("Bootstrap Version: "+$.fn.tooltip.Constructor.VERSION)```


# AngularJS


```angular.version.full``` or ```alert("AngularJS Version: "+angular.version.full)```


# VueJS


```Vue.version``` or ```alert("VueJS Version: "+Vue.version)```
