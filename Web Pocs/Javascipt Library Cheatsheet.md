To quickly display the version of the library in use - enter the following into the browser console:

# Polyglot

```
async function DependencyChecker(){
var JSDependencies=[]
var NotDetected=[]
try{JSDependencies.push("JQuery Version: "+jQuery().jquery)}catch(e){NotDetected.push("JQuery")}
try{JSDependencies.push("JQuery-UI Version:"+jQuery.ui.version)}catch(e){NotDetected.push("JQuery-UI")}
try{JSDependencies.push("Knockout Version: "+ko.version)}catch(e){NotDetected.push("Knockout")}
try{JSDependencies.push("Bootstrap Version: "+$.fn.tooltip.Constructor.VERSION)}catch(e){NotDetected.push("Bootstrap")}
try{JSDependencies.push("Angular Version: "+angular.version.full)}catch(e){NotDetected.push("Angular")}
try{JSDependencies.push("Vue Version: "+Vue.version)}catch(e){NotDetected.push("Vue")}
try{JSDependencies.push("ReactJS Version: "+React.version)}catch(e){NotDetected.push("ReactJS")}
try{JSDependencies.push("D3 Version: "+d3.version)}catch(e){NotDetected.push("D3")}
try{JSDependencies.push("Ember Version: "+Ember.VERSION)}catch(e){NotDetected.push("Ember")}
try{JSDependencies.push("Backbone Version: "+Backbone.VERSION)}catch(e){NotDetected.push("Backbone")}
try{JSDependencies.push("GSAP Version: "+gsap.version)}catch(e){NotDetected.push("GSAP")}
try{JSDependencies.push("DataTable Version: "+$.fn.DataTable.version)}catch(e){NotDetected.push("DataTable")}
if(JSDependencies.length==0){JSDependencies.push("No JavaScript Libraries Detected.")}
alert("JavaScript Libraries:\n"+JSDependencies.join("\n")+"\n\nLibraries Not Detected:\n"+NotDetected.join(", ")+".")
}
DependencyChecker()
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


# ReactJS


```React.version``` or ```alert("ReactJS Version: "+React.version)```


# D3


```d3.version``` or ```alert("D3 Version: "+d3.version)```


# Ember


```Ember.VERSION``` or ```alert("Ember Version: "+Ember.VERSION)```


# Backbone


```Backbone.VERSION``` or ```alert("Backbone Version: "+Backbone.VERSION)```


# GSAP


```gsap.version``` or ```alert("GSAP Version: "+gsap.version)```


# DataTable

```$.fn.DataTable.version``` or ```alert("DataTable Version: "+$.fn.DataTable.version)```
