odoo.define('property_management_system', function (require) 
{
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');

var QWeb = core.qweb;
var _t = core._t;

var popup = L.popup();

var Dashboard = Widget.extend({
	template: 'PMC_DashboardsMain',

	init: function(parent, data){
        return this._super.apply(this, arguments);
    },

    start: function() {
        return this.load();
    },

    load: function(){

        var self = this;

        var mymap = L.map(this.$('#mapid')[0]).setView([31.52150, 74.29638], 18);
		
		L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 20,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
		  '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		  'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
		}).addTo(mymap);

		L.polygon([
			[31.5215991, 74.2954990],
			[31.5208532, 74.2963309],
			[31.5211999, 74.2972983],
			[31.5219721, 74.2970025],
			[31.5219090, 74.2967622],
			[31.5222242, 74.2966328],
			[31.5220876, 74.2962261],
			[31.5215991, 74.2954990]
		],{
			color: 'blue',
			fillColor: '#f03',
			fillOpacity: 0.3
		}).addTo(mymap)
		// .bindPopup("Axiom Housing Socity")
		;

		var marker = L.marker([31.52152, 74.29642]).addTo(mymap);
		marker.bindPopup("<b>Axiom World</b><br>Your dream land.").openPopup();

		mymap.on('click', function(e){
			popup
		        .setLatLng(e.latlng)
		        .setContent("You clicked the map at " + e.latlng.toString())
		        .openOn(mymap);
		});

		// Road Area

		L.polygon([
			[31.521785, 74.295779],
			[31.521822, 74.295838],
			[31.521612, 74.296074],
			[31.52179, 74.296525],
			[31.521996, 74.296433],
			[31.522028, 74.296492],
			[31.52174, 74.296616],
			[31.521561, 74.296133],
			[31.521291, 74.296439],
			[31.521433, 74.296884],
			[31.521369, 74.296927],
			[31.521209, 74.296439],
			[31.521785, 74.295779]
		],{
			color: 'black',
			fillColor: 'black',
			fillOpacity: 0.3
		}).addTo(mymap)
		.bindPopup("Socity Road Area")
		;

		// Green Belt Area

		L.polygon([
			[31.521749, 74.295731],
			[31.521779, 74.295773],
			[31.521203, 74.296433],
			[31.521363, 74.296921],
			[31.521346, 74.297018],
			[31.521145, 74.296412],
			[31.521145, 74.296412]
		],{
			color: 'green',
			fillColor: 'green',
			fillOpacity: 0.8
		}).addTo(mymap)
		.bindPopup("Socity Green Belt");


        setTimeout(function(){ mymap.invalidateSize()}, 400);
    },
});

core.action_registry.add('property_management_system.main', Dashboard);

return 
{
    Dashboard: Dashboard
};

});