import { locations } from "./locations.js";

// Define map
var map = L.map("map").setView([30.860891827586183, 1.6772206149121374], 6.0);
L.tileLayer("/static/raster-tiles/{z}/{x}/{y}.png", {
  minZoom: 5,
  maxZoom: 13,
  tms: false,
  attribution: "Mehamli - Belkhodja",
}).addTo(map);

// Add markers, templates and circles to map
for (var i = 0; i < locations.length; i++) {
  var marker = L.marker([locations[i][1], locations[i][2]])
    .bindPopup(locations[i][0])
    .addTo(map);
  var circle = L.circle([locations[i][1], locations[i][2]], {
    radius: 50000,
    color: "#0080ff",
    fillColor: "#0080ff",
    fillOpacity: 0.2,
  }).addTo(map);
}
