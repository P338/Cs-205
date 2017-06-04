// Asks JavaScript to show more errors.
"use strict";

/*
 * # Boilerplate jQuery
 * This code loads the file `res/scores.json` and calls the `visualize` function
 * as soon as the JSON file is loaded.
 */
 $(function() {
   $.getJSON("res/stocks2.json")
    .done(function (data) { visualizeIndustrials(data); })
    .fail(function() { alert("Failed to load the JSON file!\n(Did your Python run?)"); });
 });

/*
 * # d3.js visualization
 * All of the code to create our visualization will be contained in the `visualize` function,
 * which is called once the data for the visualization has been loaded by the boilerplate
 * jQuery code.
 */
 var visualize4 = function(data) {
  /*
   * # Boilerplate Code for d3.js
   */
  var margin = { top: 40, right: 20, bottom: 20, left: 120 },
     width = 1000 - margin.left - margin.right,
     height = 800 - margin.top - margin.bottom;

  var svg = d3.select("#chart4")
              .append("svg")
              .attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom)
              .style("width", width + margin.left + margin.right)
              .style("height", height + margin.top + margin.bottom)
              .append("g")
              .attr("transform", "translate(" + margin.left + "," + margin.top + ")");



  // Scales
var betascale = d3.scaleLinear()
                  .domain([-.5,1])
                  .range([0,width])

var betaaxis = d3.axisTop()
                 .scale(betascale);

svg.append("g")
   .attr("transform","translate(0," + (30) + " )")
   .call(betaaxis);

var yieldscale = d3.scaleLinear()
                   .domain([-.14,.14])
                   .range([30,height]);
var yaxisformat = d3.format(".0%");
var yieldaxis = d3.axisLeft()
                  .scale(yieldscale)
                  .tickFormat(yaxisformat);
svg.append("g")
   .call(yieldaxis);

var stdscale = d3.scaleLinear()
                 .domain([0.00,0.25])
                 .range([6,21]);

var divscale = d3.scaleThreshold()
                 .domain([.1,1,2,3,4,5])
                 .range(["black","hsla(290, 100%, 50%, 1)","hsla(250, 100%, 50%, 1)","hsla(190, 100%, 50%, 1)","hsla(120, 100%, 50%, 1)"]);
                 divscale(.1);
                 divscale(1);
                 divscale(2);
                 divscale(3);
                 divscale(4);
                 divscale(5);
                 divscale(100);




var tip = d3.tip()
             .attr('class', 'd3-tip')
             .html(function(d,i){
               var myString = "Stock: " + d["symbol"] + "<br>" +
               "Annual Return 1: " + d["annualreturn1"] + "<br>" +
               "Avg Return 1: " + d["avg1"] + "<br>" +
               "Sd Return 1: " + d["stdev1"] + "<br>" +
               "Beta 1: " + d["beta1"] + "<br>" +
               "Div Yield: " + d["DY"];
               return myString;
              });
var tip2 = d3.tip()
             .attr('class', 'd3-tip')
             .html(function(d,i){
               var myString = "Stock: " + d["symbol"] + "<br>" +
               "Annual Return 2: " + d["annualreturn2"] + "<br>" +
               "Avg Return 2: " + d["avg2"] + "<br>" +
               "Sd Return 2: " + d["stdev2"] + "<br>" +
               "Beta 2: " + d["beta2"] + "<br>" +
               "Div Yield: " + d["DY"];
               return myString;
              });
svg.append("line")
   .attr("stroke","black")
   .attr("x1",betascale(0))
   .attr("x2",betascale(1.2))
   .attr("y1",yieldscale(.000132667))
   .attr("y2",yieldscale(.003718667))

svg.append("text")
   .attr("class", "x label")
   .attr("text-anchor","end")
   .attr("x",width/2)
   .attr("y",-10)
   .text("Beta")
svg.append("text")
   .attr("class", "y label")
   .attr("text-anchor","end")
   .attr("x",-35)
   .attr("y",height/2)
   .text("Average Return")

svg.selectAll("stockcircles")
   .data(data)
   .enter()
   .append("circle")
   .call(tip)
   .attr("class","stockcircles")
   .attr("cx",function (d,i){
      return betascale(d["beta1"]);
    })
   .attr("cy",function (d,i){
      return yieldscale(d["avg1"]);
    })
   .attr("r",function (d){
     return stdscale(d["stdev1"]);
   })
   .attr("fill",function (d){
     return divscale(d["DY"]);
   })
    .on("mouseover",function (d,i){
     tip.show(d);
     svg.selectAll(".stockcircles")
        .filter(function(e){
          return (e.symbol != d.symbol);
        })
        .transition()
        .style("opacity",0.1);
   })
   .on('mouseout', function(d,i){
          tip.hide(d,i);

          svg.selectAll(".stockcircles")
             .filter(function(e){
                return (e.symbol != d.symbol);
                })
             .transition()
             .style("opacity",1);
        })

svg.selectAll("stockcircles")
   .data(data)
   .enter()
   .append("circle")
   .call(tip2)
   .attr("class","stockcircles")
   .attr("cx",function (d,i){
      return betascale(d["beta2"]);
    })
   .attr("cy",function (d,i){
      return yieldscale(d["avg2"]);
    })
   .attr("r",function (d){
     return stdscale(d["stdev2"]);
   })
   .attr("fill",function (d){
     return divscale(d["DY"]);
   })
   .on("mouseover",function (d,i){
     tip2.show(d);
     svg.selectAll(".stockcircles")
        .filter(function(e){
          return (e.symbol != d.symbol);
        })
        .transition()
        .style("opacity",0.1);
   })
   .on('mouseout', function(d,i){
          tip2.hide(d,i);

          svg.selectAll(".stockcircles")
             .filter(function(e){
                return (e.symbol != d.symbol);
                })
             .transition()
             .style("opacity",1);
        })



// legends
/*var legendsvg = d3.select("#legend")
                  .append("svg");
var legendSTD = d3.legendSize()
                  .scale(stdscale)
                  .shape("circle")
                  .orient("horizontal")


legendsvg.append("g")
         .attr("transform","translate(20,40)")
         .call(legendSTD);

 var legend2svg = d3.select("#legend2")
                   .append("svg")
                   .style("width",600);
 var legendDY = d3.legendColor()
                   .scale(divscale)
                   .shape("circle")
                   .orient("horizontal")
                   .cells([1,2,3,4,5])
                   .shapePadding(40)


 legend2svg.append("g")
          .attr("transform","translate(20,40)")
          .call(legendDY);
*/
};

var visualizeIndustrials = function(data){
  var groups = _.groupBy(data, "industry");
  visualize4(groups["Industrials"]);
};
$('#Industrials').click(function (e) {
 e.preventDefault()
 $(this).tab('show')
})
