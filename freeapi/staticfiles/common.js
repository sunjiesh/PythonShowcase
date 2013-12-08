//Nav导航
function initNav(objClsName){
  var navChildArr=$("ul.nav > li");
  for(var index=0;index<navChildArr.length;index++){
     var navChild=navChildArr[index];
     if(navChild.id==objClsName){
        navChild.className="active";
     }else{
	navChild.className="";
     }
  }
}
