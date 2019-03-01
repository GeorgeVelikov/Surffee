(function(factory){if(typeof module==="object"&&typeof module.exports!=="undefined"){module.exports=factory}else{factory(FusionCharts)}})(function(FusionCharts){(function(modules){var installedModules={};function __webpack_require__(moduleId){if(installedModules[moduleId]){return installedModules[moduleId].exports}var module=installedModules[moduleId]={i:moduleId,l:false,exports:{}};modules[moduleId].call(module.exports,module,module.exports,__webpack_require__);module.l=true;return module.exports}__webpack_require__.m=modules;__webpack_require__.c=installedModules;__webpack_require__.d=function(exports,name,getter){if(!__webpack_require__.o(exports,name)){Object.defineProperty(exports,name,{configurable:false,enumerable:true,get:getter})}};__webpack_require__.r=function(exports){Object.defineProperty(exports,"__esModule",{value:true})};__webpack_require__.n=function(module){var getter=module&&module.__esModule?function getDefault(){return module["default"]}:function getModuleExports(){return module};__webpack_require__.d(getter,"a",getter);return getter};__webpack_require__.o=function(object,property){return Object.prototype.hasOwnProperty.call(object,property)};__webpack_require__.p="";return __webpack_require__(__webpack_require__.s=140)})({140:function(module,exports,__webpack_require__){"use strict";var _fusioncharts=__webpack_require__(141);var _fusioncharts2=_interopRequireDefault(_fusioncharts);function _interopRequireDefault(obj){return obj&&obj.__esModule?obj:{"default":obj}}FusionCharts.addDep(_fusioncharts2["default"])},141:function(module,exports,__webpack_require__){"use strict";exports.__esModule=true;
/**!
 * @license FusionCharts JavaScript Library
 * Copyright FusionCharts Technologies LLP
 * License Information at <http://www.fusioncharts.com/license>
 *
 * @author FusionCharts Technologies LLP
 * @meta package_map_pack
 * @id fusionmaps.Aragon.1.04-03-2017 11:58:06
 */var M="M",L="L",Z="Z",Q="Q",LFT="left",RGT="right",CEN="center",MID="middle",TOP="top",BTM="bottom",geodefinitions=[{name:"Aragon",revision:1,standaloneInit:true,baseWidth:419,baseHeight:600,baseScaleFactor:10,entities:{"ES.AR.HE":{outlines:[[M,1407,1138,Q,1435,1150,1446,1131,1461,1104,1474,1087,1498,1052,1544,1075,1556,1082,1568,1084,1598,1087,1634,1075,1634,1070,1630,1062,1627,1052,1623,1040,1610,989,1573,957,1557,974,1532,982,1520,987,1515,996,1505,1011,1486,1016,1410,1035,1398,1111,1398,1118,1398,1123,Q,1398,1135,1407,1138,Z],[M,3743,503,Q,3737,503,3731,503,3710,503,3688,499,3668,498,3648,489,3624,482,3605,489,3555,511,3509,547,3504,552,3499,554,3497,557,3494,557,3488,557,3483,554,3470,549,3461,538,3416,486,3360,471,3311,457,3251,484,3226,494,3195,506,3156,523,3114,530,3072,538,3033,521,2979,498,2931,455,2916,442,2904,425,2901,420,2896,416,2874,391,2858,371,2836,340,2789,333,2787,333,2784,332,2770,332,2758,325,2735,311,2718,298,2702,284,2682,272,2679,271,2675,269,2670,266,2664,264,2645,256,2625,254,2619,254,2614,256,2609,259,2606,262,2596,278,2581,296,2559,327,2521,339,2498,345,2470,344,2465,344,2460,344,2447,344,2435,337,2431,335,2428,333,2409,318,2393,300,2386,293,2377,291,2372,291,2369,293,2354,301,2345,315,2342,322,2338,327,2335,333,2330,339,2315,362,2282,359,2277,359,2272,357,2243,355,2228,330,2226,327,2225,322,2218,298,2210,281,2201,264,2181,252,2176,249,2167,245,2155,240,2142,233,2098,215,2089,176,2088,169,2086,162,2084,150,2081,137,2079,130,2077,122,2071,98,2055,81,2052,78,2047,74,2030,64,2008,49,1993,39,1984,52,1983,56,1981,57,1979,62,1977,66,1976,67,1972,74,1972,76,1971,78,1961,106,1944,132,1937,140,1932,149,1913,183,1894,227,1889,239,1883,249,1866,274,1850,300,1842,311,1847,325,1850,337,1854,355,1856,366,1857,376,1859,388,1859,399,1859,408,1856,415,1854,425,1850,435,1844,467,1818,493,1796,513,1788,538,1789,538,1791,540,1803,547,1796,579,1788,628,1793,676,1798,723,1808,769,1825,837,1822,906,1822,928,1815,952,1813,962,1811,970,1810,981,1808,991,1803,1028,1823,1052,1827,1055,1830,1057,1869,1084,1878,1124,1879,1130,1881,1133,1886,1141,1884,1155,1884,1160,1886,1165,1898,1199,1879,1230,1878,1235,1876,1240,1867,1302,1889,1350,1896,1367,1928,1355,1966,1341,1979,1307,1991,1280,1994,1246,2001,1180,2037,1167,2059,1160,2088,1211,2094,1221,2088,1240,2081,1262,2071,1284,2060,1309,2055,1335,2052,1345,2050,1353,2052,1358,2052,1363,2055,1372,2055,1379,2062,1411,2062,1443,2062,1451,2064,1458,2079,1507,2062,1556,2060,1565,2055,1570,2044,1587,2042,1606,2038,1628,2044,1651,2045,1656,2045,1661,2047,1690,2042,1716,2040,1721,2040,1726,2042,1738,2033,1744,2028,1750,2023,1751,2006,1760,1988,1753,1983,1751,1979,1750,1972,1744,1964,1746,1913,1763,1894,1816,1893,1822,1893,1829,1896,1863,1911,1887,1935,1922,1977,1938,2050,1963,2127,1978,2182,1990,2235,2009,2237,2009,2238,2012,2242,2017,2245,2021,2250,2024,2254,2027,2269,2043,2291,2054,2294,2056,2296,2058,2320,2088,2347,2127,2377,2173,2409,2222,2415,2232,2421,2241,2425,2244,2426,2248,2426,2253,2428,2256,2438,2314,2464,2361,2477,2390,2511,2402,2550,2415,2579,2436,2618,2466,2647,2508,2682,2561,2728,2600,2762,2630,2804,2630,2843,2630,2884,2619,2899,2615,2913,2630,2918,2635,2921,2642,2940,2678,2958,2734,2960,2737,2960,2739,2962,2749,2970,2756,2982,2766,2990,2779,2996,2788,2999,2793,3012,2812,3016,2834,3021,2859,3029,2878,3031,2883,3033,2886,3036,2893,3040,2900,3062,2935,3084,2971,3087,2978,3090,2984,3104,3008,3126,3022,3129,3025,3129,3027,3140,3047,3162,3047,3175,3047,3190,3049,3195,3050,3201,3050,3226,3054,3250,3047,3300,3034,3344,3003,3378,2981,3419,2964,3463,2945,3514,2940,3522,2939,3527,2935,3553,2925,3583,2923,3588,2923,3593,2922,3616,2912,3632,2923,3636,2927,3634,2929,3634,2934,3634,2939,3638,2937,3643,2934,3646,2912,3641,2888,3641,2886,3641,2883,3641,2881,3641,2878,3651,2847,3688,2830,3719,2817,3736,2793,3763,2759,3770,2713,3780,2668,3778,2620,3778,2615,3768,2612,3761,2610,3753,2608,3731,2602,3702,2605,3685,2608,3675,2598,3661,2586,3651,2571,3648,2566,3644,2559,3621,2519,3612,2471,3612,2466,3612,2461,3619,2429,3638,2402,3656,2375,3678,2353,3700,2327,3721,2300,3778,2224,3849,2158,3851,2156,3853,2156,3856,2151,3861,2144,3865,2139,3868,2136,3871,2132,3875,2127,3888,2112,3902,2100,3910,2092,3919,2083,3924,2080,3927,2076,3953,2056,3964,2024,3968,2021,3968,2015,3970,1993,3971,1970,3973,1955,3966,1944,3954,1926,3942,1909,3939,1905,3937,1900,3936,1895,3937,1890,3946,1872,3959,1856,3976,1838,3995,1819,4017,1799,4032,1773,4068,1716,4092,1651,4105,1617,4107,1582,4114,1485,4114,1389,4114,1382,4114,1373,4114,1365,4115,1355,4119,1335,4130,1314,4146,1287,4151,1255,4158,1211,4154,1165,4154,1160,4152,1157,4132,1124,4129,1086,4129,1075,4127,1065,4125,1058,4124,1052,4120,1026,4119,1001,4119,996,4120,992,4127,987,4125,977,4117,928,4095,882,4085,862,4081,838,4078,825,4086,815,4093,806,4098,796,4108,781,4124,769,4129,767,4132,762,4137,759,4141,755,4144,752,4147,747,4163,726,4158,698,4154,676,4142,665,4139,662,4134,660,4125,659,4119,649,4090,606,4054,569,4039,554,4024,543,4020,540,4017,538,3986,516,3953,503,3926,493,3890,494,3834,499,3776,501,Q,3759,501,3743,503,Z]],label:"Huesca",shortLabel:"HE",labelPosition:[305.8,143.6],labelAlignment:[CEN,MID]},"ES.AR.TE":{outlines:[[M,2870,3330,Q,2870,3328,2867,3327,2862,3325,2857,3323,2775,3299,2692,3264,2674,3255,2652,3250,2636,3247,2623,3240,2621,3239,2618,3237,2614,3235,2609,3233,2562,3225,2538,3176,2536,3171,2533,3166,2521,3147,2514,3127,2513,3120,2508,3113,2486,3089,2457,3083,2416,3074,2387,3100,2374,3111,2377,3142,2379,3147,2379,3150,2379,3152,2381,3154,2381,3164,2384,3171,2386,3179,2387,3186,2389,3203,2387,3222,2387,3235,2381,3240,2372,3201,2350,3161,2340,3144,2320,3140,2316,3140,2313,3140,2299,3145,2301,3161,2301,3166,2303,3169,2309,3176,2306,3186,2299,3201,2284,3215,2264,3232,2243,3255,2237,3264,2228,3277,2226,3281,2225,3284,2218,3291,2223,3299,2225,3303,2225,3305,2226,3310,2230,3313,2242,3325,2247,3340,2250,3349,2254,3355,2255,3362,2257,3369,2260,3382,2264,3394,2269,3423,2255,3440,2249,3445,2243,3459,2242,3464,2238,3469,2235,3474,2232,3479,2230,3484,2225,3489,2216,3499,2210,3508,2206,3515,2201,3515,2169,3515,2142,3499,2115,3484,2093,3459,2077,3499,2054,3532,2030,3565,1993,3582,1981,3589,1969,3577,1942,3552,1939,3510,1917,3525,1903,3545,1883,3581,1861,3616,1850,3633,1845,3628,1805,3586,1767,3538,1754,3521,1728,3513,1673,3494,1620,3503,1600,3506,1576,3528,1556,3548,1525,3548,1493,3548,1461,3543,L,1459,3543,Q,1449,3542,1439,3538,1403,3550,1383,3589,1369,3616,1376,3643,1383,3665,1391,3687,1395,3698,1388,3701,1385,3703,1380,3706,1369,3715,1352,3715,1342,3716,1335,3711,1308,3696,1278,3681,1258,3670,1239,3655,1237,3654,1237,3648,1234,3628,1220,3616,1217,3613,1212,3613,1192,3615,1176,3632,1173,3637,1169,3640,1163,3647,1159,3654,1149,3681,1136,3708,1132,3715,1131,3721,1129,3728,1124,3731,1112,3742,1109,3750,1098,3796,1080,3831,1066,3857,1032,3864,975,3877,920,3899,907,3906,897,3914,L,897,3916,Q,882,3930,876,3952,865,4006,873,4065,875,4075,876,4085,876,4101,888,4107,926,4131,968,4153,970,4155,971,4160,978,4175,973,4204,970,4224,966,4245,963,4270,956,4294,951,4316,951,4340,951,4365,968,4385,973,4389,975,4394,998,4436,981,4484,978,4494,975,4502,949,4546,936,4592,934,4597,936,4602,937,4606,937,4607,937,4612,934,4617,922,4636,900,4631,898,4631,895,4628,878,4616,849,4611,848,4611,844,4609,837,4606,836,4607,783,4656,753,4719,734,4758,729,4805,719,4888,646,4921,626,4927,609,4939,643,4975,673,5e3,690,5014,712,5024,815,5070,892,5180,934,5242,1002,5278,1056,5308,1117,5324,1129,5327,1139,5331,1147,5334,1147,5339,1147,5369,1149,5400,1175,5400,1202,5402,1246,5407,1288,5412,1288,5376,1293,5339,1295,5334,1293,5327,1291,5300,1312,5297,1319,5297,1322,5290,1342,5261,1364,5286,1383,5307,1390,5351,1391,5364,1391,5376,1395,5419,1434,5425,1490,5437,1535,5464,1605,5505,1651,5569,1666,5590,1657,5617,1647,5651,1620,5663,1591,5676,1561,5683,1569,5691,1576,5701,1591,5725,1608,5747,1612,5751,1617,5756,1620,5754,1623,5752,1681,5732,1722,5708,1751,5722,1784,5722,1793,5723,1800,5723,1834,5723,1864,5729,1874,5730,1884,5732,1898,5735,1913,5739,1922,5740,1928,5742,1940,5746,1947,5757,1949,5761,1950,5764,1957,5774,1954,5790,1947,5815,1942,5840,1942,5844,1940,5845,1932,5864,1925,5876,1923,5879,1923,5884,1923,5937,1977,5945,1991,5947,2003,5952,2008,5954,2013,5954,2047,5954,2060,5930,2062,5927,2067,5923,2074,5920,2081,5918,2072,5908,2067,5893,2052,5856,2055,5817,2060,5778,2079,5740,2081,5739,2081,5735,2083,5730,2086,5727,2093,5718,2094,5701,2094,5696,2094,5691,2093,5671,2103,5663,2118,5647,2132,5644,2142,5640,2152,5637,2220,5615,2269,5571,2303,5544,2330,5503,2360,5463,2394,5422,2404,5412,2403,5393,2401,5369,2398,5344,2398,5339,2396,5334,2389,5286,2404,5244,2408,5239,2411,5236,2430,5217,2455,5215,2508,5214,2559,5210,2584,5209,2609,5202,2667,5190,2687,5129,2696,5105,2699,5080,2704,5053,2726,5034,2740,5024,2752,5014,2774,4998,2782,4975,2801,4936,2789,4897,2775,4855,2760,4810,2755,4797,2772,4785,2813,4758,2855,4736,2862,4733,2865,4726,2867,4722,2865,4719,2850,4699,2843,4675,2823,4607,2791,4545,2779,4519,2745,4500,2704,4477,2684,4440,2680,4433,2701,4424,2743,4409,2780,4390,2824,4370,2853,4328,2899,4260,2946,4192,2958,4174,2972,4180,3016,4202,3060,4223,3099,4241,3141,4253,3197,4268,3246,4301,3256,4309,3270,4319,3273,4323,3278,4323,3299,4321,3309,4311,3346,4275,3409,4265,3450,4260,3488,4260,3490,4260,3494,4260,3497,4245,3504,4228,3505,4209,3510,4192,3521,4162,3539,4136,3560,4113,3573,4085,3592,4053,3583,4016,3573,3974,3570,3931,3565,3869,3585,3806,3592,3782,3587,3762,3578,3726,3553,3699,3548,3694,3544,3689,3534,3681,3526,3672,3519,3674,3516,3664,3509,3657,3500,3650,3488,3638,3475,3626,3468,3621,3458,3621,3456,3621,3453,3620,3433,3611,3409,3611,3404,3611,3399,3609,3394,3608,3390,3606,3372,3593,3348,3598,3294,3611,3239,3618,3228,3621,3214,3616,3206,3615,3197,3606,3194,3603,3189,3598,3178,3586,3172,3569,3155,3530,3133,3501,3124,3488,3106,3479,3060,3455,3011,3445,3006,3443,3002,3442,2957,3415,2914,3381,Q,2884,3357,2870,3330,Z]],label:"Teruel",shortLabel:"TE",labelPosition:[181.9,451.7],labelAlignment:[CEN,MID]},"ES.AR.ZR":{outlines:[[M,1623,626,Q,1593,655,1562,684,1559,687,1557,693,1554,726,1527,728,1513,730,1501,725,1495,723,1486,723,1459,721,1439,732,1425,740,1415,754,1393,792,1364,823,1339,852,1315,881,1286,918,1280,964,1276,999,1264,1030,1246,1079,1215,1124,1202,1148,1203,1174,1208,1219,1219,1265,1219,1268,1215,1275,1208,1284,1195,1290,1188,1294,1183,1297,1153,1319,1156,1373,1158,1379,1156,1384,1153,1411,1149,1438,1146,1458,1142,1479,1142,1484,1139,1487,1131,1504,1134,1528,1142,1590,1190,1639,1197,1646,1202,1653,1210,1661,1220,1670,1244,1694,1266,1717,1276,1728,1278,1741,1280,1768,1269,1792,1268,1799,1266,1805,1263,1826,1256,1846,1254,1855,1247,1856,1246,1858,1242,1860,1220,1882,1200,1897,1181,1910,1178,1926,1173,1958,1154,1980,1114,2031,1054,2041,1e3,2053,943,2029,920,2022,900,2010,870,1993,831,2002,809,2007,787,2009,739,2014,710,1977,707,1973,704,1968,700,1965,695,1960,660,1916,602,1919,568,1921,536,1919,485,2026,500,2056,505,2066,512,2073,550,2119,578,2165,604,2205,568,2261,561,2273,563,2276,588,2305,590,2346,592,2383,577,2414,558,2453,544,2493,534,2527,512,2563,494,2597,444,2602,414,2603,404,2617,372,2664,378,2724,385,2786,378,2844,367,2945,316,3039,311,3049,299,3054,280,3056,285,3030,287,3018,282,3010,267,2986,224,2983,212,2981,207,2988,177,3018,151,3054,146,3061,140,3067,112,3091,94,3106,85,3117,84,3128,79,3181,94,3223,97,3232,97,3239,97,3262,82,3277,74,3288,63,3294,46,3310,50,3347,53,3398,89,3425,129,3455,162,3484,167,3488,170,3493,165,3494,162,3496,160,3498,157,3499,160,3503,162,3503,175,3506,189,3510,294,3533,404,3538,439,3540,470,3564,524,3604,575,3645,614,3676,655,3699,707,3730,760,3759,766,3762,771,3767,793,3792,814,3821,829,3843,851,3862,861,3870,871,3877,875,3881,875,3882,885,3901,897,3914,907,3906,920,3899,975,3877,1032,3864,1066,3857,1080,3831,1098,3796,1109,3750,1112,3742,1124,3731,1129,3728,1131,3721,1132,3715,1136,3708,1149,3681,1159,3654,1163,3647,1169,3640,1173,3637,1176,3632,1192,3615,1212,3613,1217,3613,1220,3616,1234,3628,1237,3648,1237,3654,1239,3655,1258,3670,1278,3681,1308,3696,1335,3711,1342,3716,1352,3715,1369,3715,1380,3706,1385,3703,1388,3701,1395,3698,1391,3687,1383,3665,1376,3643,1369,3616,1383,3589,1403,3550,1439,3538,1449,3542,1459,3543,L,1461,3543,Q,1493,3548,1525,3548,1556,3548,1576,3528,1600,3506,1620,3503,1673,3494,1728,3513,1754,3521,1767,3538,1805,3586,1845,3628,1850,3633,1861,3616,1883,3581,1903,3545,1917,3525,1939,3510,1942,3552,1969,3577,1981,3589,1993,3582,2030,3565,2054,3532,2077,3499,2093,3459,2115,3484,2142,3499,2169,3515,2201,3515,2206,3515,2210,3508,2216,3499,2225,3489,2230,3484,2232,3479,2235,3474,2238,3469,2242,3464,2243,3459,2249,3445,2255,3440,2269,3423,2264,3394,2260,3382,2257,3369,2255,3362,2254,3355,2250,3349,2247,3340,2242,3325,2230,3313,2226,3310,2225,3305,2225,3303,2223,3299,2218,3291,2225,3284,2226,3281,2228,3277,2237,3264,2243,3255,2264,3232,2284,3215,2299,3201,2306,3186,2309,3176,2303,3169,2301,3166,2301,3161,2299,3145,2313,3140,2316,3140,2320,3140,2340,3144,2350,3161,2372,3201,2381,3240,2387,3235,2387,3222,2389,3203,2387,3186,2386,3179,2384,3171,2381,3164,2381,3154,2379,3152,2379,3150,2379,3147,2377,3142,2374,3111,2387,3100,2416,3074,2457,3083,2486,3089,2508,3113,2513,3120,2514,3127,2521,3147,2533,3166,2536,3171,2538,3176,2562,3225,2609,3233,2614,3235,2618,3237,2621,3239,2623,3240,2636,3247,2652,3250,2674,3255,2692,3264,2775,3299,2857,3323,2862,3325,2867,3327,2870,3328,2870,3330,2884,3357,2914,3381,2957,3415,3002,3442,3006,3443,3011,3445,3060,3455,3106,3479,3124,3488,3133,3501,3155,3530,3172,3569,3178,3586,3189,3598,3194,3603,3197,3606,3206,3615,3214,3616,3228,3621,3239,3618,3294,3611,3348,3598,3372,3593,3390,3606,3394,3608,3399,3609,3404,3611,3409,3611,3433,3611,3453,3620,3456,3621,3458,3621,3468,3621,3475,3626,3488,3638,3500,3650,3509,3657,3516,3664,3504,3579,3483,3494,3480,3477,3480,3460,3482,3459,3483,3457,3488,3455,3492,3454,3495,3454,3497,3452,3539,3443,3582,3433,3592,3430,3602,3425,3605,3423,3607,3420,3632,3405,3646,3376,3663,3345,3675,3315,3678,3303,3682,3291,3685,3277,3687,3262,3687,3247,3699,3239,3727,3215,3758,3191,3753,3189,3748,3189,3743,3189,3737,3188,3714,3188,3700,3169,3688,3149,3678,3127,3676,3122,3676,3117,3676,3111,3676,3106,3678,3101,3676,3096,3675,3081,3682,3074,3683,3073,3683,3067,3683,3042,3682,3018,3682,3017,3678,3013,3661,2990,3648,2973,3636,2959,3634,2942,3634,2940,3634,2939,3634,2934,3634,2929,3636,2927,3632,2923,3616,2912,3593,2922,3588,2923,3583,2923,3553,2925,3527,2935,3522,2939,3514,2940,3463,2945,3419,2964,3378,2981,3344,3003,3300,3034,3250,3047,3226,3054,3201,3050,3195,3050,3190,3049,3175,3047,3162,3047,3140,3047,3129,3027,3129,3025,3126,3022,3104,3008,3090,2984,3087,2978,3084,2971,3062,2935,3040,2900,3036,2893,3033,2886,3031,2883,3029,2878,3021,2859,3016,2834,3012,2812,2999,2793,2996,2788,2990,2779,2982,2766,2970,2756,2962,2749,2960,2739,2960,2737,2958,2734,2940,2678,2921,2642,2918,2635,2913,2630,2899,2615,2884,2619,2843,2630,2804,2630,2762,2630,2728,2600,2682,2561,2647,2508,2618,2466,2579,2436,2550,2415,2511,2402,2477,2390,2464,2361,2438,2314,2428,2256,2426,2253,2426,2248,2425,2244,2421,2241,2415,2232,2409,2222,2377,2173,2347,2127,2320,2088,2296,2058,2294,2056,2291,2054,2269,2043,2254,2027,2250,2024,2245,2021,2242,2017,2238,2012,2237,2009,2235,2009,2182,1990,2127,1978,2050,1963,1977,1938,1935,1922,1911,1887,1896,1863,1893,1829,1893,1822,1894,1816,1913,1763,1964,1746,1972,1744,1979,1750,1983,1751,1988,1753,2006,1760,2023,1751,2028,1750,2033,1744,2042,1738,2040,1726,2040,1721,2042,1716,2047,1690,2045,1661,2045,1656,2044,1651,2038,1628,2042,1606,2044,1587,2055,1570,2060,1565,2062,1556,2079,1507,2064,1458,2062,1451,2062,1443,2062,1411,2055,1379,2055,1372,2052,1363,2052,1358,2050,1353,2052,1345,2055,1335,2060,1309,2071,1284,2081,1262,2088,1240,2094,1221,2088,1211,2059,1160,2037,1167,2001,1180,1994,1246,1991,1280,1979,1307,1966,1341,1928,1355,1896,1367,1889,1350,1867,1302,1876,1240,1878,1235,1879,1230,1898,1199,1886,1165,1884,1160,1884,1155,1886,1141,1881,1133,1879,1130,1878,1124,1869,1084,1830,1057,1827,1055,1823,1052,1803,1028,1808,991,1810,981,1811,970,1813,962,1815,952,1822,928,1822,906,1825,837,1808,769,1798,723,1793,676,1788,628,1796,579,1803,547,1791,540,1789,538,1788,538,1762,521,1730,542,Q,1673,577,1623,626,Z,M,1634,1075,Q,1598,1087,1568,1084,1556,1082,1544,1075,1498,1052,1474,1087,1461,1104,1446,1131,1435,1150,1407,1138,1398,1135,1398,1123,1398,1118,1398,1111,1410,1035,1486,1016,1505,1011,1515,996,1520,987,1532,982,1557,974,1573,957,1610,989,1623,1040,1627,1052,1630,1062,Q,1634,1070,1634,1075,Z]],label:"Zaragoza",shortLabel:"ZR",labelPosition:[148.3,269.8],labelAlignment:[CEN,MID]}}}];exports["default"]={extension:geodefinitions,name:"aragon",type:"maps"}}})});