(function(factory){if(typeof module==="object"&&typeof module.exports!=="undefined"){module.exports=factory}else{factory(FusionCharts)}})(function(FusionCharts){(function(modules){var installedModules={};function __webpack_require__(moduleId){if(installedModules[moduleId]){return installedModules[moduleId].exports}var module=installedModules[moduleId]={i:moduleId,l:false,exports:{}};modules[moduleId].call(module.exports,module,module.exports,__webpack_require__);module.l=true;return module.exports}__webpack_require__.m=modules;__webpack_require__.c=installedModules;__webpack_require__.d=function(exports,name,getter){if(!__webpack_require__.o(exports,name)){Object.defineProperty(exports,name,{configurable:false,enumerable:true,get:getter})}};__webpack_require__.r=function(exports){Object.defineProperty(exports,"__esModule",{value:true})};__webpack_require__.n=function(module){var getter=module&&module.__esModule?function getDefault(){return module["default"]}:function getModuleExports(){return module};__webpack_require__.d(getter,"a",getter);return getter};__webpack_require__.o=function(object,property){return Object.prototype.hasOwnProperty.call(object,property)};__webpack_require__.p="";return __webpack_require__(__webpack_require__.s=154)})({154:function(module,exports,__webpack_require__){"use strict";var _fusioncharts=__webpack_require__(155);var _fusioncharts2=_interopRequireDefault(_fusioncharts);function _interopRequireDefault(obj){return obj&&obj.__esModule?obj:{"default":obj}}FusionCharts.addDep(_fusioncharts2["default"])},155:function(module,exports,__webpack_require__){"use strict";exports.__esModule=true;
/**!
 * @license FusionCharts JavaScript Library
 * Copyright FusionCharts Technologies LLP
 * License Information at <http://www.fusioncharts.com/license>
 *
 * @author FusionCharts Technologies LLP
 * @meta package_map_pack
 * @id fusionmaps.Sofia.18.08-13-2012 02:02:23
 */var M="M",L="L",Z="Z",Q="Q",LFT="left",RGT="right",CEN="center",MID="middle",TOP="top",BTM="bottom",geodefinitions=[{name:"Sofia",revision:18,standaloneInit:true,baseWidth:601,baseHeight:530,baseScaleFactor:10,entities:{10:{outlines:[[M,1352,246,Q,1317,222,1294,220,1295,204,1256,201,1256,167,1239,153,1231,147,1232,125,1230,106,1223,100,1166,69,1140,47,L,1124,47,Q,824,183,824,205,824,213,841,236,858,259,858,274,858,298,795,399,791,402,768,411,747,418,741,432,732,453,706,455,684,456,685,479,L,601,479,601,794,Q,606,807,599,826,L,640,826,Q,636,791,665,799,L,665,774,700,773,Q,699,756,702,749,L,740,749,740,729,775,729,Q,793,754,835,746,887,763,890,763,888,767,907,821,912,838,919,882,932,889,940,939,941,955,962,961,969,970,967,997,969,1006,988,1019,L,992,1049,Q,1028,1060,1052,1081,1059,1088,1122,1088,1177,1089,1182,1114,L,1274,1114,Q,1274,1095,1277,1091,1295,1090,1365,1093,1427,1093,1429,1073,L,1429,1041,1444,1041,Q,1434,1011,1451,998,1472,983,1472,968,1472,942,1490,937,1509,932,1509,904,1509,901,1509,899,1509,887,1522,873,1533,863,1525,839,1545,840,1543,810,1541,782,1571,792,L,1571,770,1584,770,Q,1576,791,1597,795,1607,797,1629,796,L,1629,817,Q,1649,817,1659,820,L,1697,820,1697,720,1723,720,1723,702,1755,702,Q,1773,703,1776,691,1779,675,1793,676,L,1819,677,Q,1822,643,1847,648,1837,628,1854,623,1873,616,1871,597,1893,587,1895,582,1897,578,1897,568,1897,558,1889,554,1881,547,1878,522,L,1878,500,Q,1857,494,1857,480,1857,467,1854,457,1837,439,1826,422,L,1826,388,Q,1789,391,1771,391,1622,379,1556,384,1501,389,1474,339,1447,289,1413,290,L,1413,270,Q,1386,270,1352,246,Z]],label:"Godech",shortLabel:"GO",labelPosition:[124.8,58],labelAlignment:[CEN,MID]},11:{outlines:[[M,3842,1924,Q,3837,1959,3787,1942,3794,1965,3773,1967,3744,1963,3737,1966,3741,1989,3729,1994,3724,1995,3691,1995,3654,1995,3607,1972,3605,1996,3581,1994,3587,2014,3563,2035,3539,2053,3553,2089,L,3450,2089,Q,3427,2066,3421,2066,3395,2065,3392,2074,3384,2087,3353,2099,3334,2105,3323,2128,3313,2145,3290,2141,3262,2135,3267,2166,3262,2189,3233,2194,3218,2206,3217,2243,3217,2267,3190,2261,3212,2316,3167,2356,3113,2402,3112,2421,L,3088,2421,3088,2438,3103,2438,3103,2454,3135,2454,3135,2504,3116,2504,3116,2528,Q,3118,2528,3118,2536,L,3107,2536,Q,3105,2533,3095,2533,L,3095,2588,Q,3096,2588,3121,2595,3111,2633,3162,2634,3190,2636,3245,2628,3289,2628,3303,2648,3307,2654,3340,2654,3366,2654,3360,2676,L,3422,2676,Q,3422,2695,3426,2700,L,3475,2700,Q,3476,2681,3478,2676,L,3567,2676,Q,3570,2670,3575,2653,L,3588,2653,3588,2669,3663,2669,Q,3665,2676,3665,2698,L,3736,2698,3736,2710,3775,2710,3775,2700,3803,2700,3803,2676,3846,2676,3846,2614,Q,3844,2604,3843,2604,3807,2604,3791,2601,L,3791,2579,3775,2579,3775,2545,3752,2543,3752,2515,3775,2515,3775,2499,3802,2499,Q,3799,2477,3827,2474,3818,2456,3830,2454,3846,2450,3846,2435,L,3846,2376,Q,3868,2373,3871,2335,3871,2291,3873,2278,3892,2268,3895,2238,3896,2201,3898,2184,3922,2149,3920,2105,3918,2061,3920,2040,3922,2014,3920,2005,3916,1986,3895,1981,3901,1940,3871,1940,L,3871,1924,Z]],label:"Gorna Malina",shortLabel:"GM",labelPosition:[350.4,231.7],labelAlignment:[CEN,MID]},12:{outlines:[[M,3990,3150,Q,3980,3118,3926,3100,3922,3099,3918,3098,3899,3088,3895,3105,3891,3121,3880,3125,3869,3128,3874,3147,3880,3163,3848,3162,3844,3186,3832,3187,L,3801,3188,Q,3742,3194,3729,3195,3699,3194,3582,3097,3564,3082,3532,3086,3486,3092,3480,3091,3425,3059,3371,3069,3365,3048,3340,3049,3288,3050,3287,3051,L,3281,3016,3164,3016,3164,3051,Q,3140,3039,3142,3059,3143,3087,3118,3092,3127,3116,3104,3121,3083,3126,3089,3141,L,3066,3141,3066,3162,Q,3045,3150,3039,3168,3030,3187,3027,3191,L,3029,3192,3029,3262,Q,3030,3287,3046,3290,3061,3291,3061,3314,3061,3325,3017,3422,3017,3423,3052,3469,3089,3517,3090,3533,3090,3579,3109,3602,3110,3603,3112,3641,3115,3669,3134,3661,L,3134,3694,3137,3701,3136,3702,Q,3153,3753,3186,3750,3190,3749,3226,3768,3238,3774,3283,3773,3294,3777,3320,3802,3340,3824,3359,3829,3392,3855,3393,3855,3417,3855,3443,3873,L,3498,3873,Q,3512,3873,3546,3891,3553,3895,3596,3894,3631,3894,3642,3910,3661,3936,3697,3926,3700,3927,3731,3957,3747,3974,3791,4023,L,3836,4023,3836,4001,3862,4001,3862,3976,3899,3976,3899,3946,4025,3946,Q,4038,3966,4083,3965,4131,3963,4148,3976,4175,3994,4201,3994,L,4268,3994,Q,4273,3996,4279,3995,4291,3993,4314,3994,L,4314,3972,4489,3972,Q,4507,3969,4511,3935,4525,3916,4562,3872,4589,3834,4595,3800,4572,3691,4662,3642,L,4662,3591,Q,4590,3563,4551,3474,L,4526,3474,Q,4511,3512,4436,3523,4419,3523,4269,3362,4214,3304,4068,3265,Q,4030,3158,3990,3150,Z]],label:"Ihtiman",shortLabel:"IH",labelPosition:[384,352],labelAlignment:[CEN,MID]},13:{outlines:[[M,5654,2673,Q,5647,2661,5632,2603,5620,2556,5617,2534,5593,2534,5574,2551,5557,2565,5527,2555,5530,2584,5519,2599,5499,2617,5484,2632,5454,2656,5458,2667,5454,2672,5423,2693,L,5401,2693,5401,2745,Q,5402,2748,5405,2749,L,5405,2775,Q,5393,2768,5381,2787,5370,2805,5353,2795,L,5353,2816,5337,2816,Q,5335,2852,5335,2926,5365,2927,5372,2939,5378,2949,5380,2977,5380,3005,5390,3020,5397,3031,5459,3145,5475,3173,5506,3195,5522,3207,5559,3232,L,5559,3215,Q,5569,3212,5592,3212,L,5592,3196,5621,3196,5621,3166,5818,3166,5818,3137,5847,3137,Q,5845,3071,5901,3033,5957,2995,5957,2941,5957,2906,5956,2902,5953,2894,5929,2870,5912,2828,5891,2811,5879,2801,5846,2756,5824,2724,5796,2723,Q,5681,2715,5654,2673,Z]],label:"Koprivshtitsa",shortLabel:"KP",labelPosition:[564.6,294.8],labelAlignment:[CEN,MID]},14:{outlines:[[M,4025,3946,L,3899,3946,3899,3976,3862,3976,3862,4001,3836,4001,3836,4023,3791,4023,Q,3747,3974,3731,3957,3700,3927,3697,3926,3661,3936,3642,3910,3631,3894,3596,3894,3553,3895,3546,3891,3512,3873,3498,3873,L,3443,3873,Q,3417,3855,3393,3855,3392,3855,3359,3829,3340,3824,3320,3802,3294,3777,3283,3773,3238,3774,3226,3768,3190,3749,3186,3750,3153,3753,3136,3702,L,3136,3701,3079,3701,3079,3719,3057,3719,3044,3743,3041,3800,Q,3015,3791,3020,3829,3023,3868,2998,3861,L,2998,3948,Q,3024,3938,3044,3954,3068,3973,3094,3973,3106,3973,3139,3996,3156,4008,3186,4020,3187,4031,3190,4059,3191,4063,3191,4067,3310,4083,3331,4083,3367,4082,3417,4083,3440,4083,3448,4096,3472,4111,3470,4117,L,3498,4117,3498,4096,3527,4096,3527,4067,3577,4067,Q,3605,4062,3607,4101,3606,4122,3603,4164,3605,4183,3618,4223,3627,4254,3624,4284,3655,4284,3674,4295,3692,4305,3721,4305,3748,4305,3765,4338,3778,4364,3779,4382,3779,4414,3773,4419,3755,4428,3733,4447,3700,4482,3679,4499,L,3600,4552,Q,3588,4558,3578,4583,3566,4614,3561,4620,3549,4634,3487,4682,3445,4714,3441,4746,3416,4765,3361,4799,3319,4831,3307,4862,3327,4876,3340,4892,3384,4948,3445,4948,3457,4909,3475,4909,3495,4909,3497,4921,L,3570,4921,Q,3566,4896,3587,4878,3616,4851,3622,4836,3644,4790,3694,4797,3694,4787,3702,4768,3793,4761,3849,4690,3901,4626,3944,4562,L,3948,4519,3969,4519,Q,3969,4517,3968,4481,3966,4465,3981,4466,L,3981,4453,3998,4453,Q,4008,4471,4052,4516,4104,4569,4125,4569,4149,4569,4186,4543,4207,4528,4247,4499,4275,4483,4310,4463,4331,4445,4331,4413,4313,4344,4313,4309,4278,4314,4248,4301,4198,4281,4194,4280,4189,4246,4189,4181,4188,4160,4207,4083,4243,4066,4236,4050,4229,4015,4266,4017,4259,4002,4268,3994,L,4201,3994,Q,4175,3994,4148,3976,4131,3963,4083,3965,Q,4038,3966,4025,3946,Z]],label:"Kostenets",shortLabel:"KN",labelPosition:[394.4,421.7],labelAlignment:[CEN,MID]},15:{outlines:[[M,1882,1039,L,1690,1039,Q,1672,1031,1644,999,1617,968,1594,961,1571,937,1544,937,1511,937,1509,904,1509,932,1490,937,1472,942,1472,968,1472,983,1451,998,1434,1011,1444,1041,L,1429,1041,1429,1073,1466,1073,Q,1469,1082,1488,1082,1504,1082,1504,1095,1504,1125,1522,1148,1535,1166,1568,1224,1579,1234,1577,1274,1599,1304,1599,1314,L,1599,1374,Q,1599,1396,1618,1418,1618,1422,1604,1496,L,1573,1496,1573,1523,1516,1523,1516,1501,1456,1501,1456,1529,1406,1529,1406,1625,Q,1402,1631,1388,1637,1377,1641,1379,1656,L,1379,1697,1359,1697,1359,1752,Q,1380,1765,1409,1822,1428,1839,1434,1862,1446,1870,1455,1874,1456,1876,1456,1896,1480,1895,1503,1916,1516,1929,1542,1958,1585,1997,1586,1999,L,1586,2072,1601,2072,Q,1606,2091,1638,2091,1679,2091,1669,2069,L,1711,2069,1711,2046,1738,2046,1738,2063,1778,2063,Q,1784,2063,1798,2089,1810,2095,1833,2103,1843,2118,1866,2113,1856,2140,1889,2139,1923,2136,1919,2158,1983,2158,1971,2189,L,2032,2190,Q,2037,2174,2046,2158,2081,2092,2083,2055,L,2083,1989,Q,2133,1978,2113,1918,2135,1920,2136,1889,2136,1852,2140,1848,2168,1826,2197,1806,2218,1790,2251,1754,2278,1729,2309,1728,2313,1693,2304,1686,2282,1666,2285,1654,2270,1642,2258,1646,L,2258,1557,2285,1557,2285,1542,Q,2266,1514,2254,1487,2240,1486,2235,1464,2232,1446,2210,1452,L,2210,1429,Q,2219,1420,2227,1416,L,2227,1259,Q,2213,1254,2204,1254,2202,1237,2199,1232,L,2149,1232,2149,1254,2090,1254,Q,2099,1198,2082,1189,2060,1178,2063,1137,L,2020,1137,2020,1161,1987,1161,1987,1185,1960,1185,1960,1219,1922,1219,1922,1235,1908,1235,1904,1206,Q,1903,1190,1891,1192,L,1891,1172,Q,1914,1172,1921,1161,1926,1154,1935,1134,1954,1131,1965,1131,1967,1129,1968,1103,1967,1067,1933,1067,Q,1893,1069,1882,1039,Z]],label:"Kostinbrod",shortLabel:"KB",labelPosition:[183.4,161.1],labelAlignment:[CEN,MID]},16:{outlines:[[M,4052,2040,L,3990,2040,3990,2071,3945,2071,Q,3942,2063,3942,2042,3929,2042,3920,2040,3918,2061,3920,2105,3922,2149,3898,2184,3896,2201,3895,2238,3892,2268,3873,2278,3871,2291,3871,2335,3868,2373,3846,2376,L,3846,2435,Q,3846,2450,3830,2454,3818,2456,3827,2474,3799,2477,3802,2499,L,3775,2499,3775,2515,3752,2515,3752,2543,3775,2545,3775,2579,3791,2579,3791,2601,Q,3807,2604,3843,2604,3844,2604,3846,2614,3850,2609,3853,2623,3857,2639,3875,2636,3866,2657,3879,2667,3890,2676,3893,2684,L,3895,2736,Q,3926,2778,3926,2797,3926,2873,3941,2885,L,3939,2990,Q,3938,2996,3929,3007,3918,3016,3918,3027,L,3918,3098,Q,3922,3099,3926,3100,4012,3118,4083,3113,4117,3113,4142,3087,4168,3060,4186,3060,L,4186,2842,4223,2842,4223,2822,4245,2822,Q,4253,2779,4256,2756,4258,2728,4271,2720,4284,2711,4285,2699,4286,2687,4281,2686,4275,2684,4266,2670,L,4266,2648,Q,4286,2612,4286,2599,L,4286,2598,Q,4286,2587,4283,2579,4280,2572,4274,2566,4261,2555,4261,2515,4261,2462,4284,2467,L,4284,2434,Q,4278,2432,4258,2432,4253,2407,4241,2404,L,4243,2179,Q,4236,2174,4228,2168,4154,2109,4136,2102,Q,4109,2091,4052,2040,Z]],label:"Mirkovo",shortLabel:"MI",labelPosition:[401.9,251.3],labelAlignment:[CEN,MID]},17:{outlines:[[M,5171,2473,Q,5142,2450,5127,2455,5123,2438,5109,2423,5095,2410,5095,2395,5095,2371,5116,2373,5119,2239,5121,2171,5092,2168,5084,2138,L,5034,2139,5034,2145,Q,5034,2162,5034,2181,5034,2200,4969,2263,4915,2337,4903,2370,4899,2377,4893,2439,4872,2448,4870,2464,L,4870,2501,Q,4868,2511,4849,2527,L,4849,2565,Q,4851,2579,4826,2589,4833,2604,4820,2608,4804,2609,4799,2610,4796,2635,4788,2640,4780,2644,4781,2660,4781,2677,4792,2687,4801,2696,4799,2734,4798,2760,4822,2799,4834,2817,4828,2881,4829,2897,4846,2914,L,4851,2947,4851,2947,Q,4879,2955,4892,2933,4904,2914,4928,2925,4956,2866,5100,2871,L,5100,2848,5156,2848,5291,2921,Q,5297,2925,5333,2926,L,5335,2926,Q,5335,2852,5337,2816,L,5353,2816,5353,2795,Q,5370,2805,5381,2787,5393,2768,5405,2775,L,5405,2749,Q,5402,2748,5401,2745,L,5401,2693,5423,2693,Q,5454,2672,5458,2667,5454,2656,5484,2632,5499,2617,5519,2599,5530,2584,5527,2555,5476,2556,5475,2550,5470,2534,5432,2529,5404,2526,5381,2451,L,5324,2451,5322,2478,5226,2479,Q,5178,2479,5171,2473,Z]],label:"Pirdop",shortLabel:"PI",labelPosition:[515.4,267.2],labelAlignment:[CEN,MID]},18:{outlines:[[M,4654,953,Q,4654,934,4668,929,4683,923,4683,899,4683,865,4651,831,4620,804,4608,792,4538,794,4502,817,4468,839,4449,839,4319,839,4317,794,L,4225,794,Q,4223,805,4223,834,L,4203,834,4203,909,Q,4217,915,4224,917,4225,917,4225,932,4225,938,4209,949,4195,959,4186,959,4162,959,4150,926,4134,883,4124,876,4075,838,3987,838,L,3973,838,3973,882,Q,3943,874,3942,889,3938,915,3925,925,L,3925,960,Q,3946,973,3985,1032,3999,1055,3998,1075,3995,1098,4015,1119,4015,1139,4001,1139,3984,1140,3978,1167,L,3939,1167,3939,1187,3925,1187,3925,1199,Q,3918,1223,3941,1258,4053,1283,4041,1370,4039,1410,4007,1422,3994,1426,3992,1436,3990,1447,3986,1449,3968,1459,3968,1479,3968,1503,4001,1534,4033,1565,4034,1585,4034,1587,4032,1590,L,4034,1591,Q,4118,1591,4246,1575,4245,1546,4299,1546,4329,1546,4388,1549,4406,1548,4418,1536,4430,1525,4445,1525,4479,1525,4500,1493,4511,1476,4550,1465,4563,1450,4600,1444,4630,1420,4644,1404,4640,1388,4659,1376,4678,1363,4678,1355,4707,1312,4718,1291,4724,1281,4743,1263,4759,1244,4754,1222,4746,1202,4745,1178,4724,1138,4724,1120,4724,1053,4721,1047,Q,4654,988,4654,953,Z]],label:"Pravets",shortLabel:"PR",labelPosition:[433.9,119.1],labelAlignment:[CEN,MID]},19:{outlines:[[M,2750,3437,L,2750,3379,Q,2729,3375,2721,3375,L,2721,3303,Q,2683,3312,2679,3287,2681,3254,2677,3241,L,2579,3241,2579,3258,2537,3258,Q,2530,3227,2528,3223,2524,3215,2502,3215,2475,3215,2456,3254,2438,3287,2439,3319,2439,3338,2451,3347,2463,3356,2461,3386,2459,3420,2467,3430,2475,3441,2475,3464,2475,3495,2474,3498,2468,3510,2439,3507,2418,3504,2402,3518,2384,3535,2376,3536,2368,3501,2307,3467,2268,3410,2226,3415,2218,3347,2127,3313,2089,3298,2061,3269,2042,3248,2004,3248,1993,3248,1964,3270,1936,3292,1933,3302,1931,3331,1894,3393,1877,3454,1842,3485,1796,3524,1798,3574,L,1798,3756,Q,1809,3769,1826,3811,1842,3849,1842,3858,1842,3925,1816,3939,1790,3935,1795,3976,1779,3979,1772,3979,L,1772,4013,Q,1848,4041,1975,4096,L,2047,4096,2047,4074,2074,4074,Q,2073,4084,2083,4105,L,2113,4105,2113,4122,Q,2057,4142,2037,4142,L,2037,4188,2124,4309,Q,2198,4282,2229,4333,2271,4403,2285,4408,L,2285,4456,2264,4456,2264,4478,2240,4483,Q,2181,4473,2149,4491,2115,4510,2057,4558,2e3,4605,1982,4668,1962,4730,1970,4747,1986,4780,1992,4801,2011,4800,2015,4810,2019,4821,2033,4821,2088,4821,2087,4843,L,2146,4843,2146,4825,Q,2147,4824,2192,4826,2219,4827,2208,4796,L,2270,4796,2270,4768,2411,4768,2411,4880,Q,2406,4914,2450,4962,2490,5008,2515,5015,2525,5018,2564,5020,2586,5048,2597,5046,L,2597,5078,Q,2603,5079,2623,5083,L,2623,5122,2603,5122,Q,2611,5147,2572,5145,2569,5187,2552,5184,L,2552,5203,Q,2596,5203,2685,5213,2694,5213,2703,5228,2712,5244,2728,5244,L,2797,5244,2812,5242,2812,5209,Q,2863,5192,2893,5067,2888,5053,2899,5046,2914,5032,2916,5030,2918,5001,2922,4979,2919,4960,2939,4941,2964,4916,2966,4913,L,3007,4913,Q,3007,4921,3021,4951,L,3066,4951,3066,4920,3099,4920,Q,3099,4898,3123,4898,3161,4898,3171,4942,3176,4963,3220,4991,3244,5029,3259,5041,3310,5070,3311,5085,L,3339,5085,Q,3344,5067,3382,5041,3425,5013,3427,5008,3438,4973,3444,4951,3445,4949,3445,4948,3384,4948,3340,4892,3327,4876,3307,4862,3300,4857,3292,4852,3259,4836,3247,4827,3078,4736,3078,4676,3078,4659,3084,4657,3099,4661,3105,4646,3105,4616,3118,4609,3134,4598,3134,4525,3134,4480,3121,4449,3121,4417,3118,4405,3102,4390,3094,4382,L,3094,4266,3134,4266,Q,3125,4237,3167,4240,L,3167,4211,Q,3143,4183,3121,4184,L,3121,4111,Q,3129,4110,3137,4090,3137,4084,3165,4085,3189,4087,3191,4067,3191,4063,3190,4059,3187,4031,3186,4020,3156,4008,3139,3996,3106,3973,3094,3973,3068,3973,3044,3954,3024,3938,2998,3948,L,2998,3861,Q,3023,3868,3020,3829,3015,3791,3041,3800,L,3044,3743,3033,3743,Q,3003,3745,2994,3745,2911,3726,2883,3727,2814,3727,2791,3749,L,2760,3749,2760,3705,Q,2751,3683,2757,3613,L,2753,3513,Q,2753,3489,2772,3489,L,2772,3437,Z]],label:"Samokov",shortLabel:"SA",labelPosition:[260.8,422.9],labelAlignment:[CEN,MID]},20:{outlines:[[M,1e3,1479,Q,986,1478,986,1486,985,1497,967,1505,936,1516,937,1529,L,912,1529,912,1553,884,1553,Q,885,1578,850,1577,816,1576,806,1581,797,1585,757,1625,709,1670,692,1687,L,632,1746,Q,610,1802,575,1792,L,575,1815,504,1815,Q,492,1887,526,1929,571,1982,689,1963,709,2015,743,2108,776,2160,787,2171,795,2178,824,2204,826,2207,826,2222,829,2235,846,2237,928,2240,930,2245,937,2256,1007,2291,L,1008,2292,Q,1013,2279,1018,2272,1027,2257,1046,2266,1042,2244,1066,2234,1094,2223,1096,2216,1100,2201,1118,2191,1146,2177,1149,2174,1238,2094,1249,2064,1257,2041,1271,2040,1291,2039,1304,2027,1319,2011,1356,1989,1361,1984,1417,1955,1456,1934,1456,1897,L,1456,1896,Q,1456,1876,1455,1874,1446,1870,1434,1862,1428,1839,1409,1822,1380,1765,1359,1752,L,1359,1697,1379,1697,1379,1656,Q,1377,1641,1388,1637,1402,1631,1406,1625,L,1406,1529,1210,1529,Q,1216,1553,1171,1553,1139,1553,1124,1536,1123,1535,1081,1525,1078,1503,1036,1503,Q,1020,1479,1e3,1479,Z]],label:"Slivnitsa",shortLabel:"SL",labelPosition:[97.8,188.5],labelAlignment:[CEN,MID]},21:{outlines:[[M,2423,237,Q,2391,237,2381,225,2371,214,2332,213,2331,213,2329,213,2258,213,2202,270,2176,296,2179,340,2152,358,2153,366,2153,384,2146,406,L,2069,406,Q,2052,386,2051,373,L,2010,373,Q,2008,358,1989,358,1977,358,1969,369,1959,381,1953,381,L,1886,381,Q,1851,385,1826,388,L,1826,422,Q,1837,439,1854,457,1857,467,1857,480,1857,494,1878,500,L,1878,522,Q,1881,547,1889,554,1897,558,1897,568,1897,578,1895,582,1893,587,1871,597,1873,616,1854,623,1837,628,1847,648,1822,643,1819,677,L,1793,676,Q,1779,675,1776,691,1773,703,1755,702,L,1723,702,1723,720,1697,720,1697,820,1659,820,Q,1649,817,1629,817,L,1629,796,Q,1607,797,1597,795,1576,791,1584,770,L,1571,770,1571,792,Q,1541,782,1543,810,1545,840,1525,839,1533,863,1522,873,1509,887,1509,899,1509,901,1509,904,1511,937,1544,937,1571,937,1594,961,1617,968,1644,999,1672,1031,1690,1039,L,1882,1039,Q,1893,1069,1933,1067,1967,1067,1968,1103,1967,1129,1965,1131,1954,1131,1935,1134,1926,1154,1921,1161,1914,1172,1891,1172,L,1891,1192,Q,1903,1190,1904,1206,L,1908,1235,1922,1235,1922,1219,1960,1219,1960,1185,1987,1185,1987,1161,2020,1161,2020,1137,2063,1137,Q,2060,1178,2082,1189,2099,1198,2090,1254,L,2149,1254,2149,1232,2199,1232,Q,2202,1237,2204,1254,2213,1254,2227,1259,L,2227,1416,Q,2219,1420,2210,1429,L,2210,1452,Q,2232,1446,2235,1464,2240,1486,2254,1487,2266,1514,2285,1542,L,2285,1557,2258,1557,2258,1646,Q,2270,1642,2285,1654,2282,1666,2304,1686,2313,1693,2309,1728,2312,1728,2314,1728,2356,1728,2359,1750,L,2431,1750,2431,1724,2497,1724,2497,1698,Q,2508,1698,2526,1695,2526,1668,2540,1646,2552,1624,2552,1596,L,2721,1596,Q,2729,1612,2768,1642,2801,1668,2805,1687,2836,1702,2940,1696,2960,1696,2995,1719,3019,1718,3066,1719,3124,1708,3182,1748,3226,1751,3255,1748,3271,1747,3285,1756,L,3286,1696,Q,3253,1699,3262,1639,3266,1615,3249,1606,3230,1595,3231,1586,3228,1563,3215,1559,3194,1553,3190,1548,3152,1541,3133,1529,3071,1489,3031,1448,2993,1382,2963,1364,L,2963,1296,2990,1296,2990,1259,3018,1259,3018,1233,Q,3038,1234,3038,1216,2982,1154,2966,1131,L,2966,1059,Q,2922,1058,2896,1036,2861,1009,2852,971,2838,901,2788,827,2763,787,2725,698,2676,579,2677,525,2676,455,2724,400,2772,344,2772,339,2772,323,2663,253,2630,231,2589,230,2539,230,2523,205,L,2476,205,Q,2469,231,2462,235,Q,2458,237,2423,237,Z]],label:"Svoge",shortLabel:"SV",labelPosition:[239.7,85.1],labelAlignment:[CEN,MID]},22:{outlines:[[M,4833,2107,L,4831,2134,Q,4804,2133,4790,2135,4765,2139,4776,2160,L,4742,2162,4742,2184,Q,4710,2184,4698,2186,4697,2211,4684,2208,4672,2206,4671,2226,L,4655,2226,Q,4657,2389,4656,2527,4656,2664,4654,2776,4654,2797,4649,2883,4649,2964,4670,2987,4691,3011,4706,3057,4713,3066,4709,3102,4710,3119,4724,3140,4819,3138,4848,3134,4848,3004,4851,2949,L,4846,2914,Q,4829,2897,4828,2881,4834,2817,4822,2799,4798,2760,4799,2734,4801,2696,4792,2687,4781,2677,4781,2660,4780,2644,4788,2640,4796,2635,4799,2610,4804,2609,4820,2608,4833,2604,4826,2589,4851,2579,4849,2565,L,4849,2527,Q,4868,2511,4870,2501,L,4870,2464,Q,4872,2448,4893,2439,4899,2377,4903,2370,4915,2337,4969,2263,5034,2200,5034,2181,5034,2162,5034,2145,L,5034,2139,5033,2139,Q,5034,2137,5033,2132,5031,2124,5025,2107,Z]],label:"Zlatitsa",shortLabel:"ZL",labelPosition:[479.8,228],labelAlignment:[CEN,MID]},"03":{outlines:[[M,1866,2113,Q,1843,2118,1833,2103,1810,2095,1798,2089,1784,2063,1778,2063,L,1738,2063,1738,2046,1711,2046,1711,2069,1669,2069,Q,1679,2091,1638,2091,1606,2091,1601,2072,L,1586,2072,1586,1999,Q,1585,1997,1542,1958,1516,1929,1503,1916,1480,1895,1456,1896,L,1456,1897,Q,1456,1934,1417,1955,1361,1984,1356,1989,1319,2011,1304,2027,1291,2039,1271,2040,1257,2041,1249,2064,1238,2094,1149,2174,1146,2177,1118,2191,1100,2201,1096,2216,1094,2223,1066,2234,1042,2244,1046,2266,1027,2257,1018,2272,1013,2279,1008,2292,1022,2300,1024,2327,1026,2361,1033,2370,1046,2388,1073,2438,L,1088,2438,1088,2423,1107,2423,1107,2395,1157,2395,1157,2409,Q,1177,2409,1186,2412,1183,2493,1202,2615,L,1202,2731,Q,1201,2767,1227,2822,L,1252,2822,Q,1286,2750,1318,2738,1336,2731,1444,2731,1506,2731,1583,2743,1583,2771,1586,2776,1587,2777,1609,2778,1627,2779,1642,2797,1653,2804,1717,2802,1755,2802,1778,2792,1800,2782,1849,2782,1881,2782,1894,2750,1900,2740,1948,2727,1989,2708,1998,2639,1998,2557,1999,2522,2014,2443,2021,2399,L,2021,2273,Q,2017,2231,2032,2190,L,1971,2189,Q,1983,2158,1919,2158,1923,2136,1889,2139,Q,1856,2140,1866,2113,Z]],label:"Bozhurishte",shortLabel:"BZ",labelPosition:[156.3,240.2],labelAlignment:[CEN,MID]},"07":{outlines:[[M,775,729,L,740,729,740,749,702,749,Q,699,756,700,773,L,665,774,665,799,Q,636,791,640,826,L,599,826,Q,595,837,586,851,562,888,542,910,522,932,494,944,505,971,468,972,424,967,415,967,392,967,375,979,358,991,341,992,250,1006,166,1006,162,1015,130,1042,108,1059,108,1113,L,108,1197,Q,106,1198,87,1222,76,1234,78,1255,59,1247,59,1287,59,1308,72,1329,85,1350,88,1387,111,1389,114,1435,116,1489,136,1508,L,136,1557,111,1557,111,1586,Q,187,1602,206,1656,L,206,1698,Q,217,1707,230,1778,238,1826,297,1801,L,298,1819,Q,313,1821,348,1819,374,1820,368,1845,L,381,1845,381,1815,432,1815,432,1794,509,1794,Q,506,1805,504,1815,L,575,1815,575,1792,Q,610,1802,632,1746,L,692,1687,Q,709,1670,757,1625,797,1585,806,1581,816,1576,850,1577,885,1578,884,1553,L,912,1553,912,1529,937,1529,Q,936,1516,967,1505,985,1497,986,1486,986,1478,1e3,1479,1020,1479,1036,1503,1078,1503,1081,1525,1123,1535,1124,1536,1139,1553,1171,1553,1216,1553,1210,1529,L,1456,1529,1456,1501,1516,1501,1516,1523,1573,1523,1573,1496,1604,1496,Q,1618,1422,1618,1418,1599,1396,1599,1374,L,1599,1314,Q,1599,1304,1577,1274,1579,1234,1568,1224,1535,1166,1522,1148,1504,1125,1504,1095,1504,1082,1488,1082,1469,1082,1466,1073,L,1429,1073,Q,1427,1093,1365,1093,1295,1090,1277,1091,1274,1095,1274,1114,L,1182,1114,Q,1177,1089,1122,1088,1059,1088,1052,1081,1028,1060,992,1049,L,988,1019,Q,969,1006,967,997,969,970,962,961,941,955,940,939,932,889,919,882,912,838,907,821,888,767,890,763,887,763,835,746,Q,793,754,775,729,Z]],label:"Dragoman",shortLabel:"DR",labelPosition:[66.6,128.7],labelAlignment:[CEN,MID]},"08":{outlines:[[M,2805,1687,L,2805,1768,Q,2811,1782,2825,1795,2834,1802,2834,1826,L,2828,1881,Q,2828,1895,2814,1903,2800,1913,2797,1925,L,2791,1989,Q,2791,2013,2775,2042,2774,2083,2773,2168,2765,2234,2725,2241,2730,2285,2683,2285,2623,2277,2601,2280,2580,2284,2563,2324,2554,2347,2539,2387,L,2486,2387,Q,2484,2395,2484,2424,L,2392,2424,Q,2392,2454,2375,2470,2355,2487,2351,2518,2340,2591,2340,2621,2340,2649,2358,2716,2375,2780,2376,2830,L,2376,2871,Q,2420,2891,2431,2921,L,2431,2969,2407,2969,2407,3038,Q,2502,3091,2640,3134,2679,3144,2758,3179,2781,3183,2816,3208,2849,3231,2874,3236,L,3007,3236,3007,3192,3027,3192,3027,3191,Q,3030,3187,3039,3168,3045,3150,3066,3162,L,3066,3141,3089,3141,Q,3083,3126,3104,3121,3127,3116,3118,3092,3143,3087,3142,3059,3140,3039,3164,3051,L,3164,3016,3281,3016,3287,3051,Q,3288,3050,3340,3049,3365,3048,3371,3069,3425,3059,3480,3091,3486,3092,3532,3086,3564,3082,3582,3097,3699,3194,3729,3195,3742,3194,3801,3188,L,3832,3187,Q,3844,3186,3848,3162,3880,3163,3874,3147,3869,3128,3880,3125,3891,3121,3895,3105,3899,3088,3918,3098,L,3918,3027,Q,3918,3016,3929,3007,3938,2996,3939,2990,L,3941,2885,Q,3926,2873,3926,2797,3926,2778,3895,2736,L,3893,2684,Q,3890,2676,3879,2667,3866,2657,3875,2636,3857,2639,3853,2623,3850,2609,3846,2614,L,3846,2676,3803,2676,3803,2700,3775,2700,3775,2710,3736,2710,3736,2698,3665,2698,Q,3665,2676,3663,2669,L,3588,2669,3588,2653,3575,2653,Q,3570,2670,3567,2676,L,3478,2676,Q,3476,2681,3475,2700,L,3426,2700,Q,3422,2695,3422,2676,L,3360,2676,Q,3366,2654,3340,2654,3307,2654,3303,2648,3289,2628,3245,2628,3190,2636,3162,2634,3111,2633,3121,2595,3096,2588,3095,2588,L,3095,2533,Q,3105,2533,3107,2536,L,3118,2536,Q,3118,2528,3116,2528,L,3116,2504,3135,2504,3135,2454,3103,2454,3103,2438,3088,2438,3088,2421,3112,2421,Q,3113,2402,3167,2356,3212,2316,3190,2261,3217,2267,3217,2243,3218,2206,3233,2194,3262,2189,3267,2166,3262,2135,3290,2141,3313,2145,3323,2128,3334,2105,3353,2099,3384,2087,3392,2074,3395,2065,3421,2066,3427,2066,3450,2089,L,3553,2089,Q,3539,2053,3563,2035,3587,2014,3581,1994,3605,1996,3607,1972,3553,1946,3486,1890,3412,1829,3397,1822,3366,1790,3355,1790,3343,1789,3300,1772,3293,1762,3285,1756,3271,1747,3255,1748,3226,1751,3182,1748,3124,1708,3066,1719,3019,1718,2995,1719,2960,1696,2940,1696,Q,2836,1702,2805,1687,Z]],label:"Elin Pelin",shortLabel:"EP",labelPosition:[279.6,274.1],labelAlignment:[CEN,MID]},"02":{outlines:[[M,3973,838,L,3912,838,Q,3886,838,3879,848,3872,856,3846,856,3818,856,3784,811,3751,765,3687,765,3625,765,3610,778,L,3552,831,Q,3510,852,3487,866,3444,890,3431,915,L,3351,915,Q,3327,874,3299,853,3261,827,3244,806,L,3223,806,3223,827,Q,3205,827,3193,840,3174,859,3154,867,3149,890,3123,897,3096,904,3093,918,3090,932,3044,975,2998,1018,2980,1055,L,2966,1059,2966,1131,Q,2982,1154,3038,1216,3038,1234,3018,1233,L,3018,1259,2990,1259,2990,1296,2963,1296,2963,1364,Q,2993,1382,3031,1448,3071,1489,3133,1529,3152,1541,3190,1548,3194,1553,3215,1559,3228,1563,3231,1586,3230,1595,3249,1606,3266,1615,3262,1639,3253,1699,3286,1696,L,3285,1756,Q,3293,1762,3300,1772,3343,1789,3355,1790,3366,1790,3397,1822,3412,1829,3486,1890,3553,1946,3607,1972,3654,1995,3691,1995,3724,1995,3729,1994,3741,1989,3737,1966,3744,1963,3773,1967,3794,1965,3787,1942,3837,1959,3842,1924,L,3871,1924,3871,1901,3892,1901,3892,1872,Q,3890,1852,3895,1750,3909,1744,3910,1730,3910,1704,3918,1701,3932,1692,3949,1657,4018,1608,4031,1591,4032,1590,4032,1590,4034,1587,4034,1585,4033,1565,4001,1534,3968,1503,3968,1479,3968,1459,3986,1449,3990,1447,3992,1436,3994,1426,4007,1422,4039,1410,4041,1370,4053,1283,3941,1258,3918,1223,3925,1199,L,3925,1187,3939,1187,3939,1167,3978,1167,Q,3984,1140,4001,1139,4015,1139,4015,1119,3995,1098,3998,1075,3999,1055,3985,1032,3946,973,3925,960,L,3925,925,Q,3938,915,3942,889,3943,874,3973,882,Z]],label:"Botevgrad",shortLabel:"BG",labelPosition:[350.3,138],labelAlignment:[CEN,MID]},"09":{outlines:[[M,5010,1303,L,5010,1286,4954,1286,Q,4949,1306,4928,1307,4854,1307,4804,1276,4768,1254,4754,1222,4759,1244,4743,1263,4724,1281,4718,1291,4707,1312,4678,1355,4678,1363,4659,1376,4640,1388,4644,1404,4630,1420,4600,1444,4563,1450,4550,1465,4511,1476,4500,1493,4479,1525,4445,1525,4430,1525,4418,1536,4406,1548,4388,1549,4329,1546,4299,1546,4245,1546,4246,1575,4118,1591,4034,1591,4032,1591,4031,1591,4018,1608,3949,1657,3932,1692,3918,1701,3910,1704,3910,1730,3909,1744,3895,1750,3890,1852,3892,1872,L,3892,1901,3871,1901,3871,1940,Q,3901,1940,3895,1981,3916,1986,3920,2005,3922,2014,3920,2040,3929,2042,3942,2042,3942,2063,3945,2071,L,3990,2071,3990,2040,4052,2040,Q,4109,2091,4136,2102,4154,2109,4228,2168,4236,2174,4243,2179,4263,2190,4278,2186,4289,2205,4289,2212,L,4328,2212,Q,4342,2212,4352,2226,4362,2239,4378,2239,4411,2239,4427,2262,4450,2268,4469,2254,4491,2238,4513,2239,4577,2244,4584,2227,4591,2207,4612,2207,4634,2207,4639,2226,L,4671,2226,Q,4672,2206,4684,2208,4697,2211,4698,2186,4710,2184,4742,2184,L,4742,2162,4776,2160,Q,4765,2139,4790,2135,4804,2133,4831,2134,L,4833,2107,5025,2107,Q,5031,2124,5033,2132,L,5034,2139,5084,2138,Q,5083,2134,5082,2129,5084,2078,5082,2057,5075,1983,5089,1751,L,5089,1656,Q,5093,1625,5082,1613,5066,1602,5056,1588,5044,1572,5047,1543,5050,1505,5049,1498,5027,1465,5027,1421,5027,1394,5045,1394,L,5045,1374,Q,5070,1376,5073,1371,5074,1367,5075,1340,L,5072,1303,Z]],label:"Etropole",shortLabel:"ET",labelPosition:[448.1,185],labelAlignment:[CEN,MID]},"05":{outlines:[[M,4584,2227,Q,4577,2244,4513,2239,4491,2238,4469,2254,4450,2268,4427,2262,4411,2239,4378,2239,4362,2239,4352,2226,4342,2212,4328,2212,L,4289,2212,Q,4289,2205,4278,2186,4263,2190,4243,2179,L,4241,2404,Q,4253,2407,4258,2432,4278,2432,4284,2434,L,4284,2467,Q,4261,2462,4261,2515,4261,2555,4274,2566,4280,2572,4283,2579,4286,2587,4286,2598,L,4310,2598,4310,2582,4369,2582,Q,4374,2587,4374,2595,L,4527,2595,4527,2579,4569,2579,Q,4557,2551,4580,2550,4593,2549,4617,2550,4606,2527,4656,2527,4657,2389,4655,2226,L,4639,2226,Q,4634,2207,4612,2207,Q,4591,2207,4584,2227,Z]],label:"Chelopech",shortLabel:"CL",labelPosition:[444.9,241],labelAlignment:[CEN,MID]},"04":{outlines:[[M,4527,2595,L,4374,2595,Q,4374,2587,4369,2582,L,4310,2582,4310,2598,4286,2598,4286,2599,Q,4286,2612,4266,2648,L,4266,2670,Q,4275,2684,4281,2686,4286,2687,4285,2699,4284,2711,4271,2720,4258,2728,4256,2756,4253,2779,4245,2822,4245,2861,4255,2954,4254,2969,4324,3042,4484,3208,4495,3208,4505,3208,4545,3175,4585,3141,4628,3141,4683,3141,4724,3140,4710,3119,4709,3102,4713,3066,4706,3057,4691,3011,4670,2987,4649,2964,4649,2883,4654,2797,4654,2776,4656,2664,4656,2527,4606,2527,4617,2550,4593,2549,4580,2550,4557,2551,4569,2579,L,4527,2579,Z]],label:"Chavdar",shortLabel:"CV",labelPosition:[448.4,286.7],labelAlignment:[CEN,MID]},"01":{outlines:[[M,5563,2211,Q,5547,2210,5475,2190,5424,2175,5401,2150,5382,2130,5318,2130,L,5259,2130,Q,5250,2132,5246,2144,5241,2158,5228,2163,5210,2171,5126,2171,5123,2171,5121,2171,5119,2239,5116,2373,5095,2371,5095,2395,5095,2410,5109,2423,5123,2438,5127,2455,5142,2450,5171,2473,5178,2479,5226,2479,L,5322,2478,5324,2451,5381,2451,Q,5404,2526,5432,2529,5470,2534,5475,2550,5476,2556,5527,2555,5557,2565,5574,2551,5593,2534,5617,2534,5616,2527,5617,2523,5627,2474,5628,2428,L,5646,2428,Q,5726,2308,5726,2283,5726,2253,5706,2241,5682,2228,5679,2208,Z]],label:"Anton",shortLabel:"AN",labelPosition:[541.1,232.3],labelAlignment:[CEN,MID]},"06":{outlines:[[M,3448,4096,Q,3440,4083,3417,4083,3367,4082,3331,4083,3310,4083,3191,4067,3189,4087,3165,4085,3137,4084,3137,4090,3129,4110,3121,4111,L,3121,4184,Q,3143,4183,3167,4211,L,3167,4240,Q,3125,4237,3134,4266,L,3094,4266,3094,4382,Q,3102,4390,3118,4405,3121,4417,3121,4449,3134,4480,3134,4525,3134,4598,3118,4609,3105,4616,3105,4646,3099,4661,3084,4657,3078,4659,3078,4676,3078,4736,3247,4827,3259,4836,3292,4852,3300,4857,3307,4862,3319,4831,3361,4799,3416,4765,3441,4746,3445,4714,3487,4682,3549,4634,3561,4620,3566,4614,3578,4583,3588,4558,3600,4552,L,3679,4499,Q,3700,4482,3733,4447,3755,4428,3773,4419,3779,4414,3779,4382,3778,4364,3765,4338,3748,4305,3721,4305,3692,4305,3674,4295,3655,4284,3624,4284,3627,4254,3618,4223,3605,4183,3603,4164,3606,4122,3607,4101,3605,4062,3577,4067,L,3527,4067,3527,4096,3498,4096,3498,4117,3470,4117,Q,3472,4111,3448,4096,Z]],label:"Dolna Banya",shortLabel:"DB",labelPosition:[342.8,437.8],labelAlignment:[CEN,MID]}}}];exports["default"]={extension:geodefinitions,name:"sofia",type:"maps"}}})});