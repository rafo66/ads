function createVideoThumbnail(video_img, chanel_img, title, views, date){
  var videos_grid = document.getElementsByClassName("videos-grid")[0];
  var reference_video = videos_grid.children[0];

  var new_video = reference_video.cloneNode(true);
  //new_video.style.display = "block";
  new_video.getElementsByClassName("thumbnail")[0].src = video_img;
  new_video.getElementsByClassName("video-info")[0].getElementsByClassName("channel-image")[0].src = chanel_img;
  var texts = new_video.getElementsByClassName("video-info")[0].getElementsByClassName("video-text")[0]
  texts.getElementsByClassName("video-title")[0].innerHTML = title;
  texts.getElementsByClassName("video-views")[0].innerHTML = date;
  texts.getElementsByClassName("video-date")[0].innerHTML = views;
  videos_grid.appendChild(new_video);

} 
function removeTemplate(){
  var videos_grid = document.getElementsByClassName("videos-grid")[0];
  var reference_video = videos_grid.children[0];
  videos_grid.removeChild(reference_video);
}

function get_thumbnails(){
  // read local json file
  var request = new XMLHttpRequest();
  request.open("GET", "youtube.json", false);
  request.send(null);

  var my_JSON_object = JSON.parse(request.responseText);
  console.log(my_JSON_object);
  var videos = my_JSON_object;
  for (var i = 0; i < 8; i++) {
    createVideoThumbnail(videos[i].thumbnail, videos[i].chanelImage, videos[i].title, videos[i].stats1 + " • " + videos[i].stats2, videos[i].chanelName);
  }

  removeTemplate();
}

get_thumbnails();

createVideoThumbnail("https://i.ytimg.com/vi/cU5O9FOJVs4/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBhv2JYU7bDyN8zeVOpULFN4-W1Sg", 
"https://yt3.ggpht.com/ZhR2T5fDsGObBbBhsHjRi55QzSDnDcNb9bkkmxlr1BZS7hzhyhS-YoNX0RQQ6V81-6UIoavV=s68-c-k-c0x00ffffff-no-rj", 
"Domingo react à EGO, Le nouveau dieu de Rocket League n'a que seize ans", "EGO REACTS", "158 k vues • il y a 3 jours");