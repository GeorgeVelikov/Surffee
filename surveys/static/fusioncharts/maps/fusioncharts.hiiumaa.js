(function(factory){if(typeof module==="object"&&typeof module.exports!=="undefined"){module.exports=factory}else{factory(FusionCharts)}})(function(FusionCharts){(function(modules){var installedModules={};function __webpack_require__(moduleId){if(installedModules[moduleId]){return installedModules[moduleId].exports}var module=installedModules[moduleId]={i:moduleId,l:false,exports:{}};modules[moduleId].call(module.exports,module,module.exports,__webpack_require__);module.l=true;return module.exports}__webpack_require__.m=modules;__webpack_require__.c=installedModules;__webpack_require__.d=function(exports,name,getter){if(!__webpack_require__.o(exports,name)){Object.defineProperty(exports,name,{configurable:false,enumerable:true,get:getter})}};__webpack_require__.r=function(exports){Object.defineProperty(exports,"__esModule",{value:true})};__webpack_require__.n=function(module){var getter=module&&module.__esModule?function getDefault(){return module["default"]}:function getModuleExports(){return module};__webpack_require__.d(getter,"a",getter);return getter};__webpack_require__.o=function(object,property){return Object.prototype.hasOwnProperty.call(object,property)};__webpack_require__.p="";return __webpack_require__(__webpack_require__.s=44)})({44:function(module,exports,__webpack_require__){"use strict";var _fusioncharts=__webpack_require__(45);var _fusioncharts2=_interopRequireDefault(_fusioncharts);function _interopRequireDefault(obj){return obj&&obj.__esModule?obj:{"default":obj}}FusionCharts.addDep(_fusioncharts2["default"])},45:function(module,exports,__webpack_require__){"use strict";exports.__esModule=true;
/**!
 * @license FusionCharts JavaScript Library
 * Copyright FusionCharts Technologies LLP
 * License Information at <http://www.fusioncharts.com/license>
 *
 * @author FusionCharts Technologies LLP
 * @meta package_map_pack
 * @id fusionmaps.Hiiumaa.20.12-21-2012 09:27:25
 */var M="M",L="L",Z="Z",Q="Q",LFT="left",RGT="right",CEN="center",MID="middle",TOP="top",BTM="bottom",geodefinitions=[{name:"Hiiumaa",revision:20,standaloneInit:true,baseWidth:638,baseHeight:485,baseScaleFactor:10,entities:{"01":{outlines:[[M,4646,1055,Q,4613,1052,4610,1058,4604,1066,4573,1065,4539,1063,4528,1064,4532,1079,4509,1079,4482,1076,4473,1078,L,4473,1086,4455,1086,Q,4455,1088,4455,1097,4454,1104,4447,1101,4447,1110,4446,1113,L,4436,1113,4436,1138,4422,1138,4422,1158,4450,1158,4450,1145,4514,1145,Q,4514,1138,4515,1136,L,4531,1136,Q,4529,1148,4538,1158,4548,1168,4548,1173,L,4548,1219,Q,4548,1231,4557,1233,4558,1235,4559,1242,4560,1247,4564,1247,4572,1248,4583,1257,L,4605,1257,Q,4605,1268,4617,1268,4624,1268,4643,1267,4653,1268,4658,1276,L,4677,1276,4686,1275,4686,1057,Q,4690,1046,4673,1046,4660,1046,4659,1049,Q,4655,1055,4646,1055,Z]],label:"Kärdla",shortLabel:"KR",labelPosition:[462.4,116.1],labelAlignment:[CEN,MID]},"02":{outlines:[[M,3204,2577,Q,3186,2563,3185,2563,3175,2558,3166,2559,3157,2559,3145,2554,3133,2549,3128,2548,3106,2538,3098,2538,3086,2539,3081,2532,3075,2524,3069,2523,3044,2519,3035,2518,3021,2519,3018,2517,L,3006,2510,Q,3001,2502,2996,2501,2984,2500,2981,2496,2975,2488,2953,2482,2933,2477,2932,2468,2914,2471,2908,2462,2904,2455,2897,2454,2887,2453,2884,2451,2874,2448,2865,2440,2862,2437,2838,2437,2812,2437,2803,2444,2800,2446,2784,2448,2772,2454,2768,2455,2755,2456,2748,2456,2735,2457,2730,2463,2726,2466,2692,2467,2680,2474,2674,2476,2655,2473,2651,2479,2647,2485,2635,2485,2619,2485,2616,2486,2592,2498,2578,2497,2568,2496,2557,2501,2545,2506,2536,2506,2537,2510,2529,2518,2527,2519,2523,2531,2517,2538,2504,2551,2490,2569,2464,2601,2451,2620,2431,2651,2412,2670,2407,2695,L,2401,2707,Q,2401,2707,2401,2716,2401,2730,2393,2755,2393,2773,2403,2777,L,2403,2786,Q,2412,2783,2416,2789,2421,2797,2424,2797,2426,2797,2434,2805,2440,2811,2448,2808,L,2451,2818,2464,2818,2464,2849,Q,2475,2846,2477,2852,2479,2863,2480,2864,2486,2871,2486,2890,L,2486,2897,Q,2499,2906,2506,2925,2508,2931,2509,2946,2517,2961,2517,2963,L,2530,2997,Q,2539,3019,2538,3039,2537,3053,2546,3079,2546,3115,2549,3119,2555,3131,2555,3160,2555,3180,2563,3196,2564,3197,2564,3198,L,2564,3225,Q,2564,3230,2561,3232,2558,3234,2558,3241,L,2559,3259,Q,2559,3260,2552,3264,2547,3267,2546,3272,2548,3286,2537,3299,L,2537,3338,2577,3338,2577,3349,2564,3349,2564,3376,Q,2545,3376,2535,3376,2517,3376,2521,3387,2506,3387,2499,3387,2487,3386,2486,3394,L,2458,3395,2458,3404,2447,3404,2447,3409,Q,2450,3410,2457,3410,L,2457,3416,2471,3416,Q,2476,3415,2477,3426,2478,3427,2489,3429,2498,3430,2497,3435,2514,3435,2520,3443,2523,3448,2533,3449,2534,3449,2541,3457,2543,3458,2552,3458,2561,3459,2564,3463,2567,3468,2566,3485,2565,3487,2565,3489,2565,3524,2564,3529,2563,3535,2556,3540,2552,3544,2556,3553,2551,3558,2544,3562,2543,3571,2537,3573,2535,3573,2535,3587,2535,3600,2525,3596,2526,3605,2522,3611,2518,3617,2518,3622,2518,3632,2524,3636,2532,3641,2535,3653,2535,3656,2540,3661,2544,3664,2544,3669,2543,3675,2552,3684,2555,3687,2564,3696,2566,3698,2566,3704,L,2572,3712,Q,2572,3720,2583,3725,2594,3730,2596,3735,2606,3732,2617,3739,2630,3746,2636,3745,2644,3744,2654,3754,2662,3762,2678,3757,L,2678,3765,2687,3765,Q,2689,3770,2686,3786,2686,3798,2696,3794,L,2696,3805,Q,2708,3810,2705,3839,2706,3842,2717,3852,2717,3869,2725,3866,L,2725,3931,Q,2718,3931,2715,3938,2712,3944,2708,3944,2701,3944,2697,3951,2693,3957,2686,3955,2687,3958,2684,3962,2680,3967,2675,3964,2675,3971,2664,3973,2658,3983,2652,3981,L,2651,3992,2639,3993,2638,4002,2629,4003,2629,4015,2613,4015,Q,2613,4023,2612,4027,L,2623,4027,2623,4044,2634,4045,2634,4054,Q,2636,4054,2641,4056,2642,4056,2644,4056,2648,4056,2653,4056,L,2653,4065,2673,4065,Q,2669,4076,2677,4077,2681,4078,2692,4078,L,2692,4086,Q,2709,4085,2709,4095,L,2726,4095,2726,4105,2731,4105,Q,2742,4103,2745,4111,2747,4118,2746,4137,L,2746,4167,Q,2746,4176,2750,4178,2754,4180,2754,4187,2762,4185,2771,4194,2787,4199,2787,4202,2796,4200,2804,4212,2805,4213,2814,4216,2820,4218,2818,4226,2823,4227,2836,4227,L,2836,4240,Q,2836,4244,2844,4248,L,2844,4281,Q,2844,4285,2849,4291,2854,4296,2854,4304,2854,4310,2860,4315,2865,4319,2865,4324,2865,4332,2859,4333,2854,4335,2855,4342,2856,4351,2850,4352,2842,4353,2836,4353,L,2836,4367,2787,4367,2786,4378,Q,2768,4378,2759,4378,2742,4377,2743,4389,L,2714,4388,2714,4398,Q,2684,4398,2666,4397,L,2666,4408,2646,4408,2646,4402,2635,4402,2635,4393,Q,2632,4392,2627,4392,L,2627,4380,2617,4380,2617,4371,Q,2614,4371,2606,4371,L,2606,4359,2601,4359,Q,2601,4348,2586,4349,L,2586,4335,2575,4335,2575,4348,2562,4348,2562,4371,Q,2555,4369,2556,4385,2555,4397,2542,4394,L,2542,4402,2549,4402,2549,4408,Q,2561,4404,2560,4417,L,2581,4417,2581,4427,Q,2590,4424,2598,4431,2607,4439,2616,4436,2620,4448,2637,4446,L,2637,4457,2648,4457,2648,4477,2625,4477,2625,4487,2616,4487,2616,4506,Q,2628,4510,2633,4513,2638,4516,2651,4519,2657,4526,2669,4525,2679,4523,2686,4532,2691,4533,2706,4535,2710,4544,2719,4547,2725,4548,2726,4562,2727,4579,2730,4583,2736,4590,2738,4600,2741,4605,2752,4610,2756,4615,2766,4616,2778,4618,2784,4623,L,2814,4637,Q,2819,4641,2835,4642,2847,4642,2845,4654,2863,4654,2867,4661,2868,4664,2877,4666,2886,4667,2887,4671,2887,4674,2894,4676,2902,4679,2907,4678,2912,4676,2917,4682,2923,4687,2927,4686,2955,4698,2963,4704,2967,4708,2982,4710,2989,4717,3004,4716,3010,4718,3018,4727,3022,4729,3035,4734,3040,4740,3052,4742,3066,4744,3071,4748,3077,4753,3089,4756,3095,4759,3105,4765,3114,4764,3122,4776,3124,4777,3133,4777,3140,4777,3143,4782,3147,4789,3163,4789,3177,4798,3183,4798,3186,4798,3191,4802,3196,4807,3201,4807,3211,4807,3211,4812,3211,4817,3219,4817,3226,4817,3228,4813,3230,4809,3238,4807,L,3280,4807,Q,3291,4810,3308,4799,3327,4800,3336,4794,3345,4786,3402,4786,3417,4786,3430,4776,3442,4771,3464,4773,3477,4774,3490,4767,3499,4765,3521,4767,3523,4766,3531,4758,3542,4757,3550,4758,3560,4759,3576,4749,3585,4747,3588,4745,3594,4740,3597,4738,3618,4734,3625,4729,3642,4727,3651,4719,3665,4713,3673,4709,3690,4702,3697,4698,3719,4700,3717,4690,L,3741,4678,Q,3758,4676,3764,4673,3778,4664,3805,4657,3813,4655,3823,4647,L,3839,4635,Q,3850,4630,3849,4617,3858,4604,3857,4597,3866,4592,3868,4578,3871,4560,3875,4554,3877,4540,3881,4535,3889,4520,3888,4513,3888,4509,3894,4505,3900,4501,3898,4494,3903,4481,3904,4474,3906,4462,3911,4451,3916,4443,3916,4433,3915,4426,3918,4425,3922,4423,3926,4421,3926,4410,3927,4408,3939,4404,3942,4400,3942,4390,3943,4386,3943,4362,3956,4339,3957,4336,3959,4334,3963,4322,3963,4316,3970,4304,3974,4296,3975,4278,3982,4273,3987,4268,3987,4260,3988,4250,3988,4249,L,4006,4202,Q,4021,4184,4023,4181,L,4032,4160,Q,4045,4134,4079,4076,4114,4020,4126,3996,4127,3994,4128,3993,4131,3976,4147,3953,4164,3927,4175,3909,4183,3895,4188,3885,4193,3875,4202,3863,4211,3851,4213,3841,4215,3830,4219,3828,4222,3825,4230,3822,L,4230,3805,4219,3805,Q,4221,3796,4215,3795,4206,3795,4203,3793,4196,3783,4188,3783,4166,3783,4165,3781,4163,3776,4147,3775,4149,3764,4135,3762,4118,3761,4113,3760,L,4113,3753,4126,3753,Q,4126,3739,4131,3732,4136,3725,4136,3711,4136,3703,4142,3699,4148,3696,4148,3691,L,4148,3666,Q,4155,3669,4160,3663,4166,3655,4172,3655,4179,3655,4179,3645,L,4197,3645,Q,4195,3636,4205,3635,L,4204,3622,4204,3551,Q,4205,3550,4205,3550,4200,3542,4195,3541,4181,3540,4175,3539,4170,3539,4158,3530,4149,3523,4138,3525,L,4116,3525,Q,4102,3516,4097,3516,4080,3518,4076,3515,4072,3503,4062,3503,4055,3503,4055,3506,4054,3511,4050,3515,4038,3516,4033,3521,4007,3536,3998,3544,3985,3551,3981,3553,3969,3557,3965,3561,3957,3572,3954,3574,3944,3576,3942,3576,3937,3577,3938,3584,3909,3585,3903,3590,3886,3598,3877,3604,3855,3607,3842,3612,3813,3615,3806,3617,3767,3631,3748,3633,3730,3645,3718,3643,3709,3641,3702,3644,3694,3648,3696,3656,3684,3655,3680,3656,3673,3656,3670,3665,L,3658,3665,Q,3658,3663,3655,3656,3655,3655,3654,3655,3627,3600,3610,3571,3595,3560,3596,3548,3596,3536,3594,3533,3589,3529,3585,3523,3576,3513,3576,3513,3577,3505,3572,3500,3564,3483,3559,3478,3488,3404,3487,3403,3442,3356,3416,3332,L,3416,3322,Q,3416,3321,3416,3320,3414,3315,3407,3306,3405,3304,3403,3288,3403,3261,3397,3250,3397,3235,3393,3230,3382,3217,3382,3216,3387,3185,3375,3178,L,3375,2967,Q,3375,2967,3365,2963,L,3365,2940,Q,3364,2938,3364,2937,3355,2904,3357,2878,3357,2874,3346,2848,3346,2827,3345,2814,3346,2790,3346,2777,3345,2754,3339,2749,3337,2748,3335,2717,L,3335,2701,Q,3331,2695,3327,2689,3328,2676,3322,2669,3320,2667,3318,2665,3302,2654,3297,2648,3288,2639,3255,2615,Z]],label:"Emmaste",shortLabel:"EM",labelPosition:[310.1,362.7],labelAlignment:[CEN,MID]},"03":{outlines:[[M,3777,113,L,3777,125,3730,125,3729,137,3711,137,Q,3705,136,3695,136,3696,141,3692,149,L,3634,149,3634,160,3626,160,3623,158,3604,158,3604,166,3579,166,3578,160,Q,3568,163,3565,155,3561,145,3549,146,L,3548,139,Q,3533,135,3529,136,3529,131,3522,128,3516,126,3512,128,L,3512,119,Q,3505,118,3495,118,L,3494,111,Q,3484,111,3481,102,3466,101,3463,98,3457,92,3429,80,3422,69,3417,67,3399,63,3399,62,3396,54,3379,55,3364,56,3367,44,L,3350,44,3350,53,3345,53,3345,345,Q,3346,352,3341,360,3335,368,3335,377,L,3335,552,Q,3335,563,3331,570,3327,578,3327,589,L,3327,676,Q,3327,688,3321,691,3315,694,3315,701,L,3315,714,Q,3314,720,3309,732,3305,744,3307,756,3288,756,3291,765,L,3280,765,Q,3284,777,3271,777,3258,777,3260,787,L,3247,787,3247,797,3233,797,3232,809,3223,809,Q,3216,788,3200,787,3198,781,3198,779,L,3179,778,3178,764,3168,764,Q,3169,756,3163,756,3156,756,3154,756,L,3153,747,3139,747,Q,3140,740,3123,739,L,3123,727,3116,727,3116,736,Q,3105,734,3105,751,3093,762,3093,766,3092,770,3089,771,3086,773,3083,787,3083,789,3079,791,3075,793,3077,799,L,3077,809,Q,3070,820,3071,825,L,3060,825,3060,835,3048,835,3048,846,3031,846,3031,856,3017,856,3017,868,Q,3006,867,3002,868,2995,869,2998,878,L,2976,878,2976,889,2946,889,Q,2945,881,2942,879,2941,879,2929,878,2933,868,2926,868,2914,868,2911,859,2900,860,2900,849,L,2882,849,Q,2884,842,2878,837,2872,832,2864,834,2866,825,2852,826,2843,826,2842,823,L,2841,816,2702,816,2702,914,Q,2714,918,2715,953,L,2715,981,Q,2724,988,2723,998,L,2723,1045,Q,2723,1048,2729,1052,2734,1056,2734,1060,L,2734,1090,Q,2747,1100,2764,1124,2772,1131,2776,1148,2778,1150,2784,1155,2788,1161,2786,1170,L,2797,1170,2797,1181,2788,1181,2788,1188,2781,1188,Q,2780,1191,2770,1193,2770,1206,2765,1206,2759,1207,2757,1216,2739,1215,2744,1227,L,2735,1227,2735,1245,Q,2740,1266,2756,1303,L,2763,1313,Q,2764,1315,2766,1329,2769,1333,2775,1340,2780,1346,2778,1355,L,2788,1355,2788,1362,2780,1362,2780,1368,2765,1368,2765,1376,2747,1376,2747,1386,2742,1386,Q,2741,1379,2740,1376,2729,1374,2726,1350,2725,1347,2719,1338,2717,1330,2713,1326,2695,1305,2683,1275,2678,1261,2661,1257,2645,1249,2629,1246,2618,1232,2599,1234,2569,1237,2563,1229,L,2507,1229,Q,2510,1241,2494,1240,2491,1257,2482,1256,2490,1288,2476,1286,L,2476,1330,2487,1341,Q,2487,1350,2494,1358,2496,1361,2496,1378,2504,1386,2504,1396,2503,1399,2513,1411,2516,1415,2517,1430,2518,1432,2531,1447,2537,1454,2538,1463,2540,1476,2585,1523,2594,1533,2613,1548,2614,1550,2628,1561,2635,1567,2637,1575,L,2637,1582,2646,1582,2646,1591,2634,1591,2634,1597,Q,2626,1596,2622,1597,2614,1597,2617,1605,L,2609,1605,2609,1598,2597,1598,2597,1588,2583,1588,Q,2571,1575,2571,1565,L,2561,1565,2561,1555,2551,1555,2550,1567,Q,2541,1562,2538,1572,2535,1582,2525,1578,L,2525,1587,2511,1587,2511,1597,2501,1597,2500,1605,2491,1607,2491,1615,2474,1615,2473,1628,2455,1628,Q,2444,1612,2358,1526,L,2343,1526,2343,1537,2325,1537,2325,1543,2312,1543,2312,1550,2329,1550,Q,2327,1565,2334,1587,2334,1588,2334,1588,L,2334,1600,Q,2337,1605,2346,1615,2345,1629,2346,1631,2347,1635,2357,1637,L,2357,1652,Q,2354,1657,2352,1669,2349,1681,2348,1687,2346,1692,2341,1698,2340,1712,2339,1717,2332,1729,2331,1735,2329,1748,2314,1767,2300,1785,2286,1794,2255,1822,2234,1839,2210,1858,2208,1859,2195,1862,2190,1864,2180,1868,2180,1877,L,2134,1878,Q,2130,1888,2121,1887,2104,1888,2098,1887,2089,1885,2082,1891,2075,1897,2067,1897,2037,1898,2024,1897,2015,1896,2008,1901,2e3,1906,1992,1904,1992,1908,1990,1910,L,1970,1910,Q,1971,1897,1962,1896,1948,1894,1942,1889,1925,1879,1910,1869,1896,1866,1891,1858,1886,1849,1878,1848,1851,1843,1841,1835,1789,1807,1772,1796,1747,1780,1739,1777,1729,1772,1722,1769,1715,1766,1704,1767,L,1676,1767,1676,1776,Q,1612,1777,1592,1778,1545,1789,1518,1787,1442,1782,1431,1791,1423,1797,1396,1795,L,1369,1815,Q,1341,1834,1321,1852,1284,1882,1277,1891,1273,1896,1263,1897,1253,1898,1250,1902,1248,1905,1216,1906,1208,1906,1200,1911,1192,1915,1182,1915,1175,1915,1168,1921,1163,1925,1155,1926,1154,1926,1153,1926,1108,1930,1109,1914,L,1045,1914,Q,1037,1906,1033,1906,L,970,1906,Q,960,1897,959,1896,956,1895,917,1895,L,825,1895,Q,817,1896,811,1889,806,1884,800,1885,799,1885,798,1885,740,1886,735,1879,732,1874,715,1874,696,1875,689,1874,626,1871,573,1871,L,537,1871,Q,522,1871,520,1870,518,1861,511,1859,506,1857,451,1857,442,1857,438,1853,434,1848,429,1848,412,1847,401,1847,389,1846,383,1836,359,1834,360,1826,L,346,1826,345,1818,Q,327,1817,322,1817,L,320,1806,299,1806,299,1797,270,1796,Q,272,1786,263,1786,252,1788,248,1787,248,1771,229,1772,L,221,1772,Q,220,1785,207,1786,191,1786,185,1788,171,1795,165,1794,159,1794,154,1798,147,1804,144,1805,L,135,1806,Q,129,1806,125,1811,125,1812,106,1813,95,1814,95,1818,95,1821,94,1825,88,1831,87,1845,88,1852,80,1865,72,1877,73,1885,74,1903,66,1924,65,1935,57,1945,51,1952,55,1962,53,1965,43,1976,L,43,2017,Q,58,2034,76,2036,90,2038,109,2058,119,2061,139,2081,143,2084,156,2088,168,2092,172,2098,181,2108,202,2119,218,2127,237,2139,L,255,2148,261,2153,Q,265,2157,272,2157,L,324,2157,Q,328,2158,341,2163,353,2168,365,2167,400,2164,410,2169,421,2175,429,2175,438,2175,447,2185,449,2185,464,2193,472,2198,483,2201,489,2207,502,2209,507,2214,520,2217,526,2221,536,2228,553,2232,556,2234,561,2237,575,2241,584,2244,590,2249,604,2265,605,2288,L,605,2292,Q,611,2294,614,2295,615,2295,615,2302,615,2309,611,2311,607,2312,606,2328,606,2330,601,2338,598,2345,599,2352,602,2367,586,2376,L,586,2390,Q,582,2398,579,2401,579,2408,594,2416,608,2424,605,2434,L,633,2434,633,2427,658,2427,658,2416,677,2416,716,2448,Q,748,2475,757,2479,764,2482,775,2497,780,2502,798,2512,808,2520,837,2546,848,2549,863,2555,877,2559,900,2556,910,2555,916,2559,920,2561,926,2566,931,2568,940,2567,948,2566,953,2573,964,2574,987,2573,990,2573,996,2580,1001,2587,1007,2586,1020,2585,1046,2586,1055,2585,1059,2589,1069,2595,1071,2596,1078,2595,1095,2593,1106,2585,1119,2586,1126,2586,1130,2582,1135,2578,1141,2579,1160,2581,1155,2567,L,1185,2567,1185,2558,1212,2558,1213,2544,1243,2544,1243,2537,1270,2537,1270,2528,1299,2528,1299,2518,1319,2518,1319,2528,1339,2528,1339,2539,1359,2539,1359,2547,1374,2547,1374,2560,1380,2560,1380,2550,1395,2550,1396,2535,Q,1402,2536,1404,2530,1406,2523,1410,2522,1414,2521,1415,2515,1417,2509,1420,2508,1428,2504,1433,2493,1440,2483,1443,2479,1454,2469,1458,2465,1456,2459,1465,2449,1481,2428,1484,2416,L,1494,2416,1494,2427,Q,1500,2428,1517,2426,1531,2426,1526,2436,L,1551,2436,1551,2446,Q,1557,2446,1575,2443,1585,2441,1590,2447,1597,2455,1600,2455,L,1618,2456,Q,1618,2458,1619,2464,L,1630,2464,1630,2480,1638,2480,1639,2506,1648,2506,Q,1649,2515,1649,2536,L,1659,2536,1659,2544,Q,1660,2543,1683,2542,L,1683,2528,1705,2528,1705,2518,1730,2518,1730,2506,Q,1748,2508,1746,2490,1760,2481,1758,2466,L,1767,2465,Q,1766,2458,1767,2455,1767,2450,1776,2451,1776,2448,1776,2447,L,1776,2438,Q,1784,2433,1784,2425,1784,2413,1784,2413,L,1789,2413,Q,1787,2405,1798,2405,1811,2405,1813,2403,1817,2395,1827,2395,1833,2395,1849,2395,L,1864,2395,Q,1871,2385,1876,2385,1900,2385,1899,2374,L,1935,2374,1935,2363,Q,1990,2371,1992,2354,2023,2359,2023,2347,L,2037,2347,Q,2048,2356,2056,2358,2062,2359,2074,2367,2081,2369,2089,2381,2096,2386,2111,2389,2131,2407,2179,2455,2225,2501,2305,2588,2310,2596,2325,2607,2338,2621,2348,2629,2367,2643,2384,2664,2401,2684,2401,2693,2401,2697,2401,2707,L,2407,2695,Q,2412,2670,2431,2651,2451,2620,2464,2601,2490,2569,2504,2551,2517,2538,2523,2531,2527,2519,2529,2518,2537,2510,2536,2506,2545,2506,2557,2501,2568,2496,2578,2497,2592,2498,2616,2486,2619,2485,2635,2485,2647,2485,2651,2479,2655,2473,2674,2476,2680,2474,2692,2467,2726,2466,2730,2463,2735,2457,2748,2456,2755,2456,2768,2455,2772,2454,2784,2448,2800,2446,2803,2444,2812,2437,2838,2437,2862,2437,2865,2440,2874,2448,2884,2451,2887,2453,2897,2454,2904,2455,2908,2462,2914,2471,2932,2468,2933,2477,2953,2482,2975,2488,2981,2496,2984,2500,2996,2501,3001,2502,3006,2510,L,3018,2517,Q,3021,2519,3035,2518,3044,2519,3069,2523,3075,2524,3081,2532,3086,2539,3098,2538,3106,2538,3128,2548,3133,2549,3145,2554,3157,2559,3166,2559,3175,2558,3185,2563,3186,2563,3204,2577,L,3255,2615,Q,3288,2639,3297,2648,3302,2654,3318,2665,3320,2667,3322,2669,3358,2669,3360,2667,3372,2655,3398,2660,3416,2663,3435,2653,3449,2652,3477,2652,3482,2651,3486,2646,3489,2642,3493,2643,3503,2644,3519,2643,3535,2643,3558,2638,3574,2638,3592,2624,3602,2616,3620,2599,3624,2595,3645,2574,3661,2557,3674,2550,3686,2543,3731,2497,3741,2486,3792,2446,3798,2439,3812,2420,3822,2412,3838,2400,3847,2395,3859,2384,3867,2376,3889,2366,3907,2357,3941,2343,3950,2337,3974,2328,3996,2320,4003,2314,4037,2281,4047,2267,4094,2196,4105,2152,4120,2116,4126,2097,4126,2090,4132,2083,4138,2076,4139,2070,4141,2060,4148,2044,4156,2028,4155,2021,4167,2011,4165,1998,4172,1996,4174,1988,4176,1980,4179,1979,4184,1976,4184,1958,L,4184,1947,4176,1936,Q,4170,1919,4161,1900,4151,1881,4140,1864,4136,1844,4131,1838,4126,1822,4122,1813,4115,1798,4107,1792,4103,1789,4103,1780,4102,1770,4098,1766,L,4098,1746,Q,4098,1745,4098,1743,4100,1682,4098,1655,4096,1616,4127,1589,4138,1580,4153,1567,4156,1563,4178,1544,4187,1536,4205,1520,4210,1515,4221,1509,4225,1506,4225,1497,4225,1493,4172,1438,4137,1398,4115,1378,L,4115,1371,Q,4115,1370,4114,1368,4112,1364,4107,1353,4106,1334,4104,1331,4100,1326,4097,1313,4095,1301,4087,1293,4083,1277,4081,1274,4074,1262,4074,1256,4074,1244,4069,1235,4061,1220,4061,1219,4044,1201,4035,1187,4017,1160,4013,1152,3998,1121,3966,1086,L,3966,1069,Q,3966,1068,3967,1066,3968,1062,3972,1062,3977,1062,3976,1057,L,3976,1034,Q,3975,1025,3979,1014,3983,1004,3981,995,L,4007,995,Q,4007,1008,4019,1009,4027,1009,4045,1008,4052,1009,4064,1009,4076,1018,4095,1020,4113,1022,4143,1023,L,4143,1020,Q,4135,1015,4131,1012,4124,1007,4128,996,L,4116,996,4116,994,Q,4116,993,4116,992,4113,979,4103,967,4092,952,4090,945,4071,914,4065,899,4061,890,4037,855,4018,829,4015,808,4005,811,4005,802,4004,789,3998,785,3995,775,3991,772,3984,766,3984,758,3984,750,3989,751,3994,751,3994,743,L,3994,719,Q,3995,709,4002,704,4009,699,4006,678,L,4006,646,Q,4006,645,3998,636,L,3997,624,Q,3997,620,3992,614,3986,607,3986,591,3986,575,3992,569,3998,564,3997,539,3995,516,3994,506,3992,488,3999,484,4005,479,4005,462,4004,442,4005,435,L,4006,355,Q,4008,354,4015,348,4022,343,4018,337,L,4028,337,4029,314,Q,4032,314,4038,314,4044,295,4044,289,4044,273,4027,277,L,4027,270,Q,4022,267,3970,227,3931,208,3915,189,3911,184,3889,170,3876,152,3864,148,3849,145,3847,143,3843,135,3836,133,3825,130,3813,113,Z]],label:"Kõrgessaare",shortLabel:"KO",labelPosition:[323.6,174.3],labelAlignment:[CEN,MID]},"04":{outlines:[[M,4174,1988,Q,4172,1996,4165,1998,4167,2011,4155,2021,4156,2028,4148,2044,4141,2060,4139,2070,4138,2076,4132,2083,4126,2090,4126,2097,4120,2116,4105,2152,4094,2196,4047,2267,4037,2281,4003,2314,3996,2320,3974,2328,3950,2337,3941,2343,3907,2357,3889,2366,3867,2376,3859,2384,3847,2395,3838,2400,3822,2412,3812,2420,3798,2439,3792,2446,3741,2486,3731,2497,3686,2543,3674,2550,3661,2557,3645,2574,3624,2595,3620,2599,3602,2616,3592,2624,3574,2638,3558,2638,3535,2643,3519,2643,3503,2644,3493,2643,3489,2642,3486,2646,3482,2651,3477,2652,3449,2652,3435,2653,3416,2663,3398,2660,3372,2655,3360,2667,3358,2669,3322,2669,3328,2676,3327,2689,3331,2695,3335,2701,L,3335,2717,Q,3337,2748,3339,2749,3345,2754,3346,2777,3346,2790,3345,2814,3346,2827,3346,2848,3357,2874,3357,2878,3355,2904,3364,2937,3364,2938,3365,2940,L,3365,2963,Q,3375,2967,3375,2967,L,3375,3178,Q,3387,3185,3382,3216,3382,3217,3393,3230,3397,3235,3397,3250,3403,3261,3403,3288,3405,3304,3407,3306,3414,3315,3416,3320,3416,3321,3416,3322,L,3416,3332,Q,3442,3356,3487,3403,3488,3404,3559,3478,3564,3483,3572,3500,3577,3505,3576,3513,3576,3513,3585,3523,3589,3529,3594,3533,3596,3536,3596,3548,3595,3560,3610,3571,3627,3600,3654,3655,3655,3655,3655,3656,3658,3663,3658,3665,L,3670,3665,Q,3673,3656,3680,3656,3684,3655,3696,3656,3694,3648,3702,3644,3709,3641,3718,3643,3730,3645,3748,3633,3767,3631,3806,3617,3813,3615,3842,3612,3855,3607,3877,3604,3886,3598,3903,3590,3909,3585,3938,3584,3937,3577,3942,3576,3944,3576,3954,3574,3957,3572,3965,3561,3969,3557,3981,3553,3985,3551,3998,3544,4007,3536,4033,3521,4038,3516,4050,3515,4054,3511,4055,3506,4055,3503,4062,3503,4072,3503,4076,3515,4080,3518,4097,3516,4102,3516,4116,3525,L,4138,3525,Q,4149,3523,4158,3530,4170,3539,4175,3539,4181,3540,4195,3541,4200,3542,4205,3550,4222,3530,4251,3498,4269,3480,4271,3471,4273,3454,4273,3430,L,4286,3430,4286,3447,4295,3447,Q,4292,3458,4305,3460,4302,3473,4309,3479,4313,3483,4323,3491,4330,3500,4341,3524,4342,3527,4353,3536,4362,3545,4364,3553,4366,3560,4377,3569,4386,3576,4385,3587,4391,3589,4396,3589,L,4396,3599,4416,3599,4416,3586,4431,3586,4431,3575,Q,4433,3575,4440,3575,4446,3575,4447,3569,L,4456,3569,Q,4457,3572,4482,3619,4493,3639,4522,3674,4524,3676,4528,3687,4536,3696,4537,3699,4539,3713,4556,3726,4566,3741,4574,3749,4575,3750,4578,3762,4579,3766,4587,3768,4589,3768,4591,3768,L,4624,3768,Q,4632,3768,4639,3762,4646,3756,4654,3756,L,4728,3756,Q,4728,3750,4729,3748,L,4751,3748,4753,3749,4753,3760,4746,3760,Q,4748,3773,4741,3778,4729,3789,4729,3789,4727,3804,4724,3807,L,4708,3824,4687,3855,Q,4681,3858,4669,3882,4657,3906,4649,3918,4641,3929,4629,3949,4614,3968,4611,3973,4607,3978,4602,3989,4596,3999,4586,4003,L,4586,4008,4609,4008,4609,4019,4635,4019,Q,4659,3997,4707,3951,4719,3941,4740,3927,4750,3918,4763,3899,4780,3886,4805,3841,4802,3832,4812,3821,4821,3811,4819,3804,L,4835,3772,Q,4829,3760,4839,3752,4850,3744,4849,3738,4848,3732,4851,3729,4853,3727,4857,3725,4860,3711,4860,3704,4867,3706,4868,3699,4868,3690,4868,3687,4875,3674,4874,3668,L,4891,3668,Q,4900,3682,4904,3681,4908,3680,4919,3679,L,4938,3677,4941,3685,4977,3685,Q,4978,3611,4978,3589,L,5061,3589,5061,3575,5157,3575,5157,3561,Q,5149,3561,5147,3560,5149,3546,5149,3538,5151,3524,5144,3520,5136,3513,5138,3483,5138,3479,5130,3471,5123,3464,5124,3456,5125,3445,5120,3439,5114,3432,5114,3429,L,5117,3400,Q,5117,3391,5116,3390,L,5106,3383,5106,3356,5118,3356,5118,3345,5126,3345,Q,5134,3331,5134,3318,L,5149,3318,5149,3301,Q,5150,3300,5159,3292,5177,3289,5171,3274,5180,3274,5185,3259,5194,3252,5196,3248,5197,3247,5197,3246,L,5197,3234,Q,5194,3234,5185,3226,5175,3223,5172,3221,5171,3210,5163,3210,5157,3210,5149,3204,L,5126,3186,Q,5121,3185,5113,3177,5109,3172,5098,3177,L,5098,3167,5080,3167,5078,3157,5062,3157,5062,3168,Q,5049,3168,5044,3176,5043,3178,5036,3180,5031,3181,5031,3185,5017,3183,5010,3193,5004,3208,4996,3215,4983,3224,4979,3228,4976,3233,4973,3235,4969,3240,4962,3237,L,4962,3262,4974,3262,4974,3274,4981,3275,4981,3289,4987,3289,4987,3305,4978,3305,4978,3309,4970,3309,4970,3316,4961,3316,4961,3308,Q,4952,3309,4950,3301,4946,3289,4943,3287,4929,3270,4921,3264,4904,3243,4901,3240,4895,3232,4892,3229,4880,3229,4880,3220,L,4876,3220,4876,3205,Q,4896,3211,4888,3164,4894,3164,4897,3165,L,4903,3165,4903,3155,4935,3155,Q,4932,3144,4957,3144,4970,3144,4990,3146,L,4990,3134,5023,3134,5023,3124,5046,3124,Q,5045,3114,5045,3109,5044,3100,5049,3098,5055,3094,5056,3077,L,5056,3021,Q,5061,3022,5069,3022,L,5069,3033,5086,3033,5086,3049,5098,3049,Q,5098,3051,5099,3057,L,5116,3057,5116,3066,5130,3067,5130,3075,5146,3075,5147,3087,5164,3087,5164,3098,Q,5166,3099,5180,3097,5192,3098,5187,3109,5195,3104,5196,3118,L,5206,3118,Q,5242,3141,5262,3150,5265,3152,5284,3168,5297,3179,5314,3177,5310,3185,5325,3191,L,5325,3197,5345,3197,5345,3209,Q,5347,3209,5353,3209,5362,3209,5362,3207,5363,3199,5366,3195,5367,3192,5381,3180,5383,3178,5386,3171,5389,3165,5393,3164,5405,3149,5407,3147,L,5407,3137,5416,3137,5416,3123,Q,5426,3123,5426,3105,5424,3084,5424,3078,5424,3035,5418,3030,5392,3008,5393,2999,5385,2999,5382,2998,L,5382,2994,5395,2994,5396,2979,Q,5404,2981,5405,2975,5404,2967,5405,2964,L,5411,2964,5411,2958,Q,5416,2958,5416,2950,L,5416,2936,5423,2936,5423,2921,5434,2921,5434,2906,5436,2906,Q,5436,2896,5426,2883,5413,2870,5407,2862,5380,2829,5374,2819,5328,2763,5313,2737,5299,2722,5297,2717,5292,2702,5287,2691,L,5263,2645,Q,5221,2568,5216,2561,L,5216,2557,Q,5216,2556,5216,2554,5217,2544,5213,2535,5206,2521,5205,2517,5200,2492,5190,2480,5181,2469,5181,2463,5181,2448,5176,2443,5172,2429,5169,2424,5161,2412,5162,2405,5008,2407,4988,2406,4985,2406,4985,2405,L,4961,2405,Q,4947,2399,4942,2399,4926,2396,4924,2394,4916,2386,4908,2386,4900,2386,4891,2380,4882,2375,4872,2375,4840,2375,4836,2365,L,4817,2365,Q,4819,2374,4800,2374,4793,2374,4792,2380,4790,2385,4787,2385,4782,2384,4770,2393,4756,2400,4752,2404,4735,2409,4731,2411,4726,2421,4716,2421,4711,2421,4707,2425,4703,2430,4700,2430,4682,2431,4682,2441,4674,2438,4670,2442,4664,2449,4658,2449,4647,2450,4645,2452,4645,2454,4645,2465,4645,2475,4649,2478,4654,2481,4655,2495,L,4655,2533,Q,4655,2552,4661,2564,4661,2569,4660,2583,4660,2595,4667,2595,L,4667,2640,4666,2648,4672,2648,4672,2654,4678,2654,4678,2678,4586,2678,Q,4572,2647,4565,2633,4554,2622,4552,2612,4551,2606,4542,2592,4541,2583,4540,2580,4532,2573,4532,2572,4526,2564,4523,2552,4516,2522,4497,2519,4487,2511,4478,2508,4463,2502,4458,2496,4440,2495,4433,2490,4416,2489,4409,2481,4394,2478,4386,2472,4378,2467,4372,2458,4367,2451,4364,2435,4360,2417,4357,2412,L,4357,2364,Q,4357,2363,4357,2361,4355,2355,4349,2339,4346,2331,4346,2309,L,4346,2174,Q,4345,2164,4337,2150,4326,2132,4325,2130,4301,2073,4282,2043,4272,2029,4245,2011,4217,1994,4209,1981,4207,1979,4196,1963,4190,1955,4184,1947,L,4184,1958,Q,4184,1976,4179,1979,Q,4176,1980,4174,1988,Z]],label:"Käina",shortLabel:"KN",labelPosition:[406.4,298.3],labelAlignment:[CEN,MID]},"05":{outlines:[[M,4902,1064,L,4884,1064,Q,4882,1071,4867,1084,4852,1098,4849,1104,L,4849,1117,Q,4860,1117,4867,1121,L,4867,1166,Q,4818,1172,4796,1142,4794,1139,4771,1118,4750,1109,4747,1096,4738,1093,4736,1093,L,4736,1086,Q,4727,1084,4713,1071,4699,1059,4686,1057,L,4686,1275,4677,1276,4658,1276,Q,4653,1268,4643,1267,4624,1268,4617,1268,4605,1268,4605,1257,L,4583,1257,Q,4572,1248,4564,1247,4560,1247,4559,1242,4558,1235,4557,1233,4548,1231,4548,1219,L,4548,1173,Q,4548,1168,4538,1158,4529,1148,4531,1136,L,4515,1136,Q,4514,1138,4514,1145,L,4450,1145,4450,1158,4422,1158,4422,1138,4436,1138,4436,1113,4446,1113,Q,4447,1110,4447,1101,4454,1104,4455,1097,4455,1088,4455,1086,L,4455,1086,Q,4442,1068,4433,1067,4429,1066,4410,1051,4378,1025,4369,1016,L,4353,1016,Q,4354,1024,4332,1026,4334,1035,4322,1034,4305,1034,4302,1035,4301,1046,4293,1045,L,4275,1045,4275,1057,4251,1057,4251,1066,4238,1066,4238,1075,4232,1075,Q,4233,1069,4229,1068,4223,1068,4218,1066,4214,1058,4203,1057,4198,1047,4188,1047,4183,1047,4180,1043,4177,1038,4173,1038,4170,1037,4159,1027,4151,1025,4147,1023,4145,1023,4143,1023,4113,1022,4095,1020,4076,1018,4064,1009,4052,1009,4045,1008,4027,1009,4019,1009,4007,1008,4007,995,L,3981,995,Q,3983,1004,3979,1014,3975,1025,3976,1034,L,3976,1057,Q,3977,1062,3972,1062,3968,1062,3967,1066,3966,1068,3966,1069,L,3966,1086,Q,3998,1121,4013,1152,4017,1160,4035,1187,4044,1201,4061,1219,4061,1220,4069,1235,4074,1244,4074,1256,4074,1262,4081,1274,4083,1277,4087,1293,4095,1301,4097,1313,4100,1326,4104,1331,4106,1334,4107,1353,4112,1364,4114,1368,4115,1370,4115,1371,L,4115,1378,Q,4137,1398,4172,1438,4225,1493,4225,1497,4225,1506,4221,1509,4210,1515,4205,1520,4187,1536,4178,1544,4156,1563,4153,1567,4138,1580,4127,1589,4096,1616,4098,1655,4100,1682,4098,1743,4098,1745,4098,1746,L,4098,1766,Q,4102,1770,4103,1780,4103,1789,4107,1792,4115,1798,4122,1813,4126,1822,4131,1838,4136,1844,4140,1864,4151,1881,4161,1900,4170,1919,4176,1936,L,4184,1947,Q,4190,1955,4196,1963,4207,1979,4209,1981,4217,1994,4245,2011,4272,2029,4282,2043,4301,2073,4325,2130,4326,2132,4337,2150,4345,2164,4346,2174,L,4346,2309,Q,4346,2331,4349,2339,4355,2355,4357,2361,4357,2363,4357,2364,L,4357,2412,Q,4360,2417,4364,2435,4367,2451,4372,2458,4378,2467,4386,2472,4394,2478,4409,2481,4416,2489,4433,2490,4440,2495,4458,2496,4463,2502,4478,2508,4487,2511,4497,2519,4516,2522,4523,2552,4526,2564,4532,2572,4532,2573,4540,2580,4541,2583,4542,2592,4551,2606,4552,2612,4554,2622,4565,2633,4572,2647,4586,2678,L,4678,2678,4678,2654,4672,2654,4672,2648,4666,2648,4667,2640,4667,2595,Q,4660,2595,4660,2583,4661,2569,4661,2564,4655,2552,4655,2533,L,4655,2495,Q,4654,2481,4649,2478,4645,2475,4645,2465,4645,2454,4645,2452,4647,2450,4658,2449,4664,2449,4670,2442,4674,2438,4682,2441,4682,2431,4700,2430,4703,2430,4707,2425,4711,2421,4716,2421,4726,2421,4731,2411,4735,2409,4752,2404,4756,2400,4770,2393,4782,2384,4787,2385,4790,2385,4792,2380,4793,2374,4800,2374,4819,2374,4817,2365,L,4836,2365,Q,4840,2375,4872,2375,4882,2375,4891,2380,4900,2386,4908,2386,4916,2386,4924,2394,4926,2396,4942,2399,4947,2399,4961,2405,L,4985,2405,Q,4985,2406,4988,2406,5008,2407,5162,2405,5161,2412,5169,2424,5172,2429,5176,2443,5181,2448,5181,2463,5181,2469,5190,2480,5200,2492,5205,2517,5206,2521,5213,2535,5217,2544,5216,2554,5216,2556,5216,2557,L,5216,2561,Q,5221,2568,5263,2645,L,5287,2691,Q,5292,2702,5297,2717,5299,2722,5313,2737,5328,2763,5374,2819,5380,2829,5407,2862,5413,2870,5426,2883,5436,2896,5436,2906,L,5446,2906,5447,2907,5447,2919,5458,2919,5459,2927,Q,5468,2922,5468,2939,L,5476,2940,Q,5476,2987,5477,3009,L,5483,3009,Q,5484,3026,5484,3068,L,5493,3068,Q,5493,3072,5490,3083,5491,3092,5505,3093,5508,3093,5514,3104,5516,3105,5522,3106,5527,3107,5525,3114,5532,3114,5569,3128,L,5569,3137,5581,3137,Q,5581,3147,5594,3150,5594,3158,5604,3157,5613,3156,5613,3167,L,5624,3167,Q,5621,3158,5648,3158,L,5648,3147,5655,3147,5656,3139,Q,5656,3138,5646,3128,L,5646,3114,Q,5642,3106,5638,3094,5639,3079,5636,3072,5624,3063,5624,3051,5616,3037,5617,3032,5619,3021,5614,3011,5609,3e3,5610,2993,5611,2984,5603,2974,5595,2963,5595,2957,L,5595,2948,5604,2948,Q,5604,2939,5603,2933,5603,2932,5603,2930,L,5603,2921,Q,5616,2921,5614,2908,5628,2912,5626,2894,L,5637,2894,Q,5650,2905,5648,2901,5658,2907,5671,2904,5680,2904,5680,2914,5685,2918,5703,2916,L,5709,2922,Q,5714,2927,5719,2926,5732,2925,5737,2932,5741,2937,5757,2936,5763,2939,5772,2946,5791,2946,5795,2947,5798,2948,5802,2956,L,5813,2956,Q,5833,2953,5829,2964,5844,2964,5852,2970,5859,2975,5872,2975,5879,2975,5893,2982,5905,2988,5918,2985,L,5918,2993,Q,5917,2995,5917,2998,L,5938,2998,Q,5933,2987,5946,2986,5961,2985,5962,2983,5964,2974,5972,2975,5980,2976,5982,2965,L,6005,2965,6005,2957,6027,2957,Q,6022,2947,6030,2946,6035,2946,6046,2946,L,6046,2936,6058,2936,6057,2961,Q,6067,2959,6066,2969,6066,2986,6066,2987,L,6077,2987,6078,3218,6095,3218,6095,3230,6114,3230,Q,6112,3221,6124,3212,6130,3207,6141,3201,6151,3190,6167,3169,6225,3123,6234,3114,6278,3070,6287,3062,6295,3055,6315,3041,6328,3027,6327,3017,6326,3007,6326,3002,6327,2997,6321,2989,6315,2980,6318,2965,6320,2953,6312,2946,6308,2935,6304,2930,6267,2886,6256,2865,L,6210,2800,Q,6192,2782,6194,2761,6196,2740,6184,2723,L,6186,2678,Q,6174,2680,6177,2669,6167,2671,6165,2664,6165,2654,6163,2651,6148,2639,6145,2635,6137,2622,6116,2600,6078,2550,6056,2525,L,6057,2361,Q,6059,2343,6044,2323,6007,2275,5993,2257,5924,2170,5881,2149,L,5868,2149,Q,5868,2141,5855,2133,5833,2119,5832,2118,5809,2098,5792,2088,5776,2084,5768,2077,5764,2074,5749,2067,5741,2063,5733,2050,5720,2030,5719,2028,5682,1975,5665,1954,5662,1939,5656,1932,5642,1918,5640,1914,5619,1891,5615,1879,5615,1877,5615,1875,5611,1868,5600,1857,5597,1854,5597,1844,5596,1837,5586,1836,5589,1825,5578,1813,5565,1798,5563,1793,5515,1729,5515,1710,5515,1704,5520,1701,5525,1698,5525,1688,L,5525,1652,5533,1652,5533,1644,5558,1644,5558,1638,5588,1638,5588,1627,5618,1627,5618,1621,5628,1621,5628,1616,5616,1616,5617,1606,Q,5607,1592,5600,1592,5595,1591,5590,1585,L,5587,1578,Q,5587,1577,5587,1576,5573,1572,5554,1556,5531,1536,5520,1527,L,5503,1513,Q,5499,1501,5495,1497,5478,1457,5478,1457,5478,1450,5479,1450,L,5485,1447,Q,5485,1434,5487,1433,5496,1429,5497,1421,5496,1412,5497,1408,5508,1413,5503,1390,5503,1386,5510,1381,5517,1376,5517,1374,5513,1366,5521,1364,5529,1361,5528,1358,L,5528,1331,5536,1331,5537,1330,5537,1318,Q,5534,1318,5533,1317,L,5522,1317,Q,5521,1327,5515,1328,5506,1337,5505,1338,L,5493,1348,Q,5480,1349,5484,1358,5476,1354,5467,1365,5458,1377,5450,1372,5437,1390,5429,1394,5414,1392,5412,1398,5410,1405,5397,1405,5390,1405,5389,1402,5387,1399,5379,1399,5361,1399,5358,1396,5351,1388,5341,1385,5327,1381,5323,1378,5321,1377,5301,1377,5297,1377,5293,1372,5289,1367,5284,1366,5268,1366,5263,1365,5257,1354,5251,1353,L,5231,1353,Q,5234,1370,5209,1365,L,5209,1377,Q,5200,1376,5196,1377,5190,1378,5191,1387,L,5164,1387,Q,5165,1376,5164,1371,5164,1361,5154,1364,L,5154,1353,Q,5148,1353,5145,1350,5145,1342,5137,1337,5137,1326,5126,1316,5114,1305,5116,1292,5118,1282,5113,1265,5109,1247,5110,1237,5111,1205,5062,1151,5045,1120,5036,1109,5026,1098,5019,1097,5008,1088,4999,1086,4977,1088,4972,1084,4962,1075,4951,1076,4946,1076,4941,1072,4935,1067,4930,1066,Q,4905,1070,4902,1064,Z]],label:"Pühalepa",shortLabel:"PU",labelPosition:[477.9,179.7],labelAlignment:[CEN,MID]}}}];exports["default"]={extension:geodefinitions,name:"hiiumaa",type:"maps"}}})});