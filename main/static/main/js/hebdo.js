

$(document).ready(function(e){
	// IE SUPPORT //
	$("#hebdo .ie-support").hide()
	$(".horaire span").hide();
	$("#hebdo  table td:first a").addClass("jour-affiche");
	$("#hebdo  .horaire span:first").show();
	$("#contenu #hebdo td a").focus(function() {
		$("#contenu #hebdo td a").removeClass("jour-affiche");
		$(this).addClass("jour-affiche");
		$(".horaire span").hide();
		$($(this).attr('href')+"-anchor").show();
	});
	// $("#contenu #hebdo td a").hover(function() {
	// 	$("#contenu #hebdo td a").removeClass("jour-affiche");
	// 	$(this).addClass("jour-affiche");
	// 	$(".horaire span").hide();
	// 	$($(this).attr('href')).show();
	// });
});