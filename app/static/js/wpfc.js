var options = {
    //Boolean - Whether we should show a stroke on each segment
    segmentShowStroke : true,

    //String - The colour of each segment stroke
    segmentStrokeColor : "#fff",

    //Number - The width of each segment stroke
    segmentStrokeWidth : 2,

    //Number - The percentage of the chart that we cut out of the middle
    percentageInnerCutout : 50, // This is 0 for Pie charts

    //Number - Amount of animation steps
    animationSteps : 100,

    //String - Animation easing effect
    animationEasing : "easeOutBounce",

    //Boolean - Whether we animate the rotation of the Doughnut
    animateRotate : true,

    //Boolean - Whether we animate scaling the Doughnut from the centre
    animateScale : false,

    //String - A legend template
    legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<segments.length; i++){%><li><span style=\"background-color:<%=segments[i].fillColor%>\"></span><%if(segments[i].label){%><%=segments[i].label%><%}%></li><%}%></ul>"

}

var data = [
    {
        value: 300,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "Red"
    },
    {
        value: 50,
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "Green"
    },
    {
        value: 100,
        color: "#FDB45C",
        highlight: "#FFC870",
        label: "Yellow"
    }
]

var labels = {
    "IV": { label: "Investimentos", color: "#46BFBD", highlight: "#5AD3D1"},
    "ES": { label: "Despesas essenciais", color: "#FDB45C", highlight: "#FFC870"},
    "LS": { label: "Estilo de vida", color: "#F7464A", highlight: "#FF5A5E"}
}

function loaded(){
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 ) {
           if(xmlhttp.status == 200){
               data = buildObjectArray(xmlhttp.responseText);

               var ctx = document.getElementById("myChart").getContext("2d");
               var myDoughnutChart = new Chart(ctx).Doughnut(data,options);
           }
           else {
               console.log('Houston...')
           }
        }
    }

    xmlhttp.open("GET", "/chart", true);
    xmlhttp.send();
}

function buildObjectArray(json){
    var obj = JSON.parse(json);
    return Object.keys(obj).filter(function(key){return key != "IN"}).map(function(key){
        if(key != "IN") {
            return {
                id: key,
                value: obj[key],
                label: labels[key]["label"],
                color: labels[key]["color"],
                highlight: labels[key]["highlight"]
            }
        }
    });
}
