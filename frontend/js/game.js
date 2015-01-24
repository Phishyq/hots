var floor = 0;
var wall = 1;

var ship = 36;
var spaceship = 37;
var plane = 38;
var tropicalIsland = 39;
var arctic = 40;
var desert = 41;

var lifeRing = 0;
var rope = 1;
var raincoat = 2;
var sextant = 3;
var anchor = 4;

var spacehelmet = 5;
var oxygen = 6;
var jetpack = 7;
var alien = 8;
var phaser = 9;

var parachute = 10;
var landingGear = 11;
var breathingMask = 12;
var suitcase = 13;
var passport = 14;

var cocktail = 15;
var beachball = 16;
var trunks = 17;
var desertIslandDisc = 18;
var pineapple = 19;

var penguin = 20;
var snowman = 21;
var pole = 22;
var santa = 23;
var scarf = 24;

var palmTree = 25;
var camel = 26;
var waterBottle = 27;
var bucket = 28;
var duneBuggy = 29;

var fists = 30;
var spoon = 31;
var gun = 32;
var knife = 33;
var nailBoard = 34;
var taser = 35;

var tile_height = 1;
var tile_width = 1;

var game = new Phaser.Game(800, 600, Phaser.AUTO, '', { preload: preload, create: create, update: update });

var myPlayer = -1;
var players = {};
var items = {};
var definitions={};

var socket = new WebSocket("ws://10.7.3.103:9000");

socket.onopen = function(){};

socket.onmessage = function(msg){
    var parsed = JSON.parse(msg);
  //  if(parsed.message == "world"){
        var world = parsed.world;

        for(var i = 0; i < world.length; i++){
            var row = world[i];
            for(var j = 0; j < row.length; j++){
                game.add.sprite(i*tile_width, j*tile_height, definitions[row[j]]);
            }
        }

   // }
};

function preload() {
    definitions[floor] = "floor";
    definitions[wall] = "wall";



    game.load.image("player","resources/art/human.png", tile_width, tile_height);
    game.load.image("wall", "resources/art/wall.png", tile_width, tile_height);
    game.load.image("floor", "resources/art/wall-black.png", tile_width, tile_height);
}

function create() {
    
}

function update() {
    
}