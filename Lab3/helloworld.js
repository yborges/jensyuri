console.log('Hello world');

document.body.style.backgroundColor = "red";

console.log(document.getElementsByTagName("a"));

for(i = 0; i<document.getElementsByTagName("a").length; i++) {
    document.getElementsByTagName("a")[i].classList.add("active_links");
}
//$("a").addClass("active_links");