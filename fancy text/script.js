function randomGreeting(){
	
	var myArry = ["A bad penny always turns up","A barking dog never bites","A change is as good as a rest","a good beginning makes a good ending"];
	
	var i = Math.floor(Math.random()*4);
	
	return(myArry[i] + "...");
	
}