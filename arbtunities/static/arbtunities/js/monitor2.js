var count = 10000;
var j = 0, url = '', data = [], layout = {};
var api_url = '/arboto/arbtunities/api/monitor2'; 

// ETH-EUR
var exchs = ['bitstamp', 'kraken', 'cryptomkt'];
layout = {
  title:'ETH-EUR'
};
url = api_url + '?count='+ count + '&pair=ETHEUR';
$.getJSON(url)
  .done(function(json) {
    var i = 0, x = [], y = [], y2=[]
    var arrayLength = json.data.length;
    for (i = 0; i < arrayLength; i++) {
      x.push(json.data[i].timestamp);
      y.push(json.data[i].hi_bid);
      y2.push(json.data[i].lo_ask);
    }
    hi_bid_dict = {
      x: x,
      y: y,
      name: 'Highest Bid',
      type: 'scatter'
    };
    lo_ask_dict = {
      x: x,
      y: y2,
      name: 'Lowest Ask',
      type: 'scatter'
    };
    data.push(hi_bid_dict);
    data.push(lo_ask_dict);
    Plotly.newPlot('graph-etheur', data, layout);
  })
  .fail(function( jqxhr, textStatus, error ) {
    var err = textStatus + ", " + error;
    console.log( "Request Failed: " + err );
  });

// ETH-BTC
j = 0;
var data2 = [];
var layout2 = {
  title:'ETH-BTC'
};
url = api_url + '?count='+ count + '&pair=ETHBTC';         
$.getJSON(url)
  .done(function(json) {
    var i = 0, x = [], y = [], y2 = [];
    var arrayLength = json.data.length;
    for (i = 0; i < arrayLength; i++) {
      x.push(json.data[i].timestamp);
      y.push(json.data[i].hi_bid);
      y2.push(json.data[i].lo_ask);
    }
    hi_bid_dict = {
      x: x,
      y: y,
      name: 'Highest Bid',
      type: 'scatter'
    };
    lo_ask_dict = {
      x: x,
      y: y2,
      name: 'Lowest Ask',
      type: 'scatter'
    };
    data2.push(hi_bid_dict, lo_ask_dict);
    Plotly.newPlot('graph-ethbtc', data2, layout2);
  })
  .fail(function( jqxhr, textStatus, error ) {
    var err = textStatus + ", " + error;
    console.log( "Request Failed: " + err );
  });


// ETH-CLP
j = 0;
var data3 = [];
var layout3 = {
  title:'ETH-CLP'
};
url = api_url + '?count='+ count + '&pair=ETHCLP';
$.getJSON(url)
  .done(function(json) {
    var i = 0, x = [], y = [], y2 = [];
    var arrayLength = json.data.length;
    for (i = 0; i < arrayLength; i++) {
      x.push(json.data[i].timestamp);
      y.push(json.data[i].hi_bid);
      y2.push(json.data[i].lo_ask);
    }
    hi_bid_dict = {
      x: x,
      y: y,
      name: 'Highest Bid',
      type: 'scatter'
    };
    lo_ask_dict = {
      x: x,
      y: y2,
      name: 'Lowest Ask',
      type: 'scatter'
    };
    data3.push(hi_bid_dict, lo_ask_dict);            
    Plotly.newPlot('graph-ethclp', data3, layout3);
  })
  .fail(function( jqxhr, textStatus, error ) {
    var err = textStatus + ", " + error;
    console.log( "Request Failed: " + err );
  });


// ticker_url = 'https://api.cryptomkt.com/v1/ticker?market=ETHCLP'
// $.getJSON(ticker_url)
//     .done(function(json) {
//       $('#eth-clp-tb-cm').append(createBody(json.data[0]));            
//     });

// ticker_url = 'https://www.buda.com/api/v2/markets/eth-clp/ticker';
// $.getJSON(proxyurl + ticker_url)
//     .done(function(json) {
//       $('#eth-clp-tb-bu').append(createBody(json.ticker));      
//     });
// // tried to solve cross-domain issue through jsonp, but didn't work.
// // Buda server probably do not implement jsonp. Using 3d-party proxy for now
// // $.ajax({
// //   dataType: "jsonp",
// //   url:  'https://www.buda.com/api/v2/markets/eth-clp/ticker?callback=handleJson',
// //   success: handleJson
// // });
// // function handleJson(data){
// //   console.log(data);
// //   ticker_data = data;
// // }

// // LTC-BTC
// exchs = ['bitstamp', 'buda']; // here
// j = 0;
// var data4 = []; // here
// var layout4 = { // here
//   title:'Mean of Price Distribution --- LTC-BTC' // here
// };
// for(j = 0; j < exchs.length; j++){
//   url = api_url + '?count='+ count + '&pair=LTCBTC&' + 'exch=' + exchs[j]; // here
//   $.getJSON(url)
//     .done(function(json) {
//       var i = 0, x = [], y = [];
//       var arrayLength = json.data.length;
//       for (i = 0; i < arrayLength; i++) {
//         x.push(json.data[i].timestamp);
//         y.push(json.data[i].price_avg);
//       }
//       trace_dict = {
//         x: x,
//         y: y,
//         name: json.exchange,
//         type: 'scatter'
//       };
//       data4.push(trace_dict); // here
//       Plotly.newPlot('graph-ltcbtc', data4, layout4);  // here
//     })
//     .fail(function( jqxhr, textStatus, error ) {
//       var err = textStatus + ", " + error;
//       console.log( "Request Failed: " + err );
//     });
// }
// // fetch ticker data for LTC-BTC from Buda
// ticker_url = 'https://www.buda.com/api/v2/markets/ltc-btc/ticker';
// $.getJSON(proxyurl + ticker_url)
//     .done(function(json) {
//         $('#ltc-btc-tb-bu').append(createBody(json.ticker));      
//     });


// // BCH-BTC
// exchs = ['bitstamp', 'buda']; // here
// j = 0;
// var data5 = []; // here
// var layout5 = { // here
//   title:'Mean of Price Distribution --- BCH-BTC' // here
// };
// for(j = 0; j < exchs.length; j++){
//   url = api_url + '?count='+ count + '&pair=BCHBTC&' + 'exch=' + exchs[j]; // here
//   $.getJSON(url)
//     .done(function(json) {
//       var i = 0, x = [], y = [];
//       var arrayLength = json.data.length;
//       for (i = 0; i < arrayLength; i++) {
//         x.push(json.data[i].timestamp);
//         y.push(json.data[i].price_avg);
//       }
//       trace_dict = {
//         x: x,
//         y: y,
//         name: json.exchange,
//         type: 'scatter'
//       };
//       data5.push(trace_dict); // here
//       Plotly.newPlot('graph-bchbtc', data5, layout5);  // here
//     })
//     .fail(function( jqxhr, textStatus, error ) {
//       var err = textStatus + ", " + error;
//       console.log( "Request Failed: " + err );
//     });
// }
// // fetch ticker data for BCH-BTC from Buda
// ticker_url = 'https://www.buda.com/api/v2/markets/bch-btc/ticker';
// $.getJSON(proxyurl + ticker_url)
//     .done(function(json) {      
//       $('#bch-btc-tb-bu').append(createBody(json.ticker));            
//     });

// // BTC-CLP
// exchs = ['cryptomkt', 'buda']; // here
// j = 0;
// var data6 = []; // here
// var layout6 = { // here
//   title:'Mean of Price Distribution --- BTC-CLP' // here
// };
// for(j = 0; j < exchs.length; j++){
//   url = api_url + '?count='+ count + '&pair=BTCCLP&' + 'exch=' + exchs[j]; // here
//   $.getJSON(url)
//     .done(function(json) {
//       var i = 0, x = [], y = [];
//       var arrayLength = json.data.length;
//       for (i = 0; i < arrayLength; i++) {
//         x.push(json.data[i].timestamp);
//         y.push(json.data[i].price_avg);
//       }
//       trace_dict = {
//         x: x,
//         y: y,
//         name: json.exchange,
//         type: 'scatter'
//       };
//       data6.push(trace_dict); // here
//       Plotly.newPlot('graph-btcclp', data6, layout6);  // here
//     })
//     .fail(function( jqxhr, textStatus, error ) {
//       var err = textStatus + ", " + error;
//       console.log( "Request Failed: " + err );
//     });
// }

// ticker_url = 'https://api.cryptomkt.com/v1/ticker?market=BTCCLP'
// $.getJSON(ticker_url)
//     .done(function(json) {      
//       $('#btc-clp-tb-cm').append(createBody(json.data[0]));            
//     });
// // fetch ticker data for BTC-CLP from Buda
// ticker_url = 'https://www.buda.com/api/v2/markets/btc-clp/ticker';
// $.getJSON(proxyurl + ticker_url)
//     .done(function(json) {                  
//       $('#btc-clp-tb-bu').append(createBody(json.ticker));
//     });


// function createBody(json){
//   var body = $('<tbody></tbody>');
//   $.each( json, function( key, val ) {
//         var newItem = $('<tr></tr>').append('<td>'+ key + '</td><td>'+ val + '</td>');
//         body.append(newItem);
//       });  
//   return body;
// }