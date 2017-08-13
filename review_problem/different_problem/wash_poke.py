"""
@description: 洗牌
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-8
"""
import sys


def wash_poke(n, my_list):
    l1 = [my_list[i] for i in range(n)]
    l2 = [my_list[n + i] for i in range(n)]
    l3 = []
    index = n - 1
    while index >= 0:
        l3.append(l2[index])
        l3.append(l1[index])
        index -= 1
    l3.reverse()
    return l3


def loop_time(k, n, my_list):
    result = my_list
    for i in range(k):
        result = wash_poke(n, result)
    return result


count = 0
num = None
l = None
times = None
my_result = []
group_num = None
data = []

try:
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            data.pop(0)
            while count < len(data):
                num, times = data[count].split(" ")
                l = data[count + 1].split(" ")
                my_result.append(" ".join(loop_time(int(times), int(num), l)))
                count += 2
            for i in my_result:
                print(i)
        data.append(line)

except Exception as e:
    print(e)


# if __name__ == '__main__':
#     l = [1, 2, 3, 4, 5, 6]
#     num = 3
#     times = 2
#     # print(wash_poke(num, l))
#     print(loop_time(times, num, l))
#     test data
# 5
# 10 49
# 384329296 939151343 104794929 144759741 670973514 615219401 6195949 494573296 531671982 924524885 445556150 979714539 305135424 13100710 933279554 201884968 849473494 629728402 45839998 279195691
# 43 59
# 114933193 94376098 129126178 703663685 283109766 549559057 904883830 50826403 126820871 967579651 10514204 618567574 296881091 75984456 110960605 899082639 186973381 486017484 261038978 120496072 686360139 165683067 496500557 356387835 478451362 153266766 914621987 156768861 644790536 792055790 978018424 508796608 857686880 233153496 246130075 654666403 419511640 336298957 792589973 218613870 46276720 969709982 455248969 678166300 245289471 204515435 317080845 63812286 337224458 522121173 672372969 513539469 321078190 882218066 4914952 439693187 432164582 600435520 494127387 479730360 174549682 986822150 503669269 936351256 288372954 606625177 444477530 31217375 684411757 985986567 492411317 348007859 370115432 62918843 915039977 946497272 368277175 379588149 357083584 434486570 764360768 157230000 952702768 230328322 8070891 355995276
# 91 68
# 476504673 647519448 559723187 82208627 286882477 533003424 34255531 70699 981216671 574642762 579918953 62547916 123320829 124432226 476328782 986286705 887358320 704839472 510187630 614273517 141109090 591507920 564788055 308099223 433546622 999040261 842514381 425011727 641485767 83378029 968174137 412105818 420700129 983880757 252779577 536675451 265966135 972340116 562754520 697236252 778909332 861809390 800702362 65044610 721541103 894142090 903028571 727238026 5562836 152787831 307612383 48182752 999156523 649046168 94997394 40851237 184951797 76014970 623809403 349471567 200852024 23157931 106763366 661520626 654320663 51110401 605007963 826744174 870136328 17628626 79057543 13704864 349877597 375525871 801853942 299318269 28424387 425776184 604812684 46678737 490980182 64725678 656218273 731986966 364102477 289420636 35147375 956907278 235588963 731339720 223257190 629661021 60851178 109489830 388044487 748835648 426564516 762385304 167861257 598117888 989370587 385576988 434274317 344508244 534144596 886580512 517122298 201121655 905373785 695565500 261362810 120689555 997766695 558022020 615003691 528241626 459611484 191533329 22673650 971430031 653846523 317668940 210506716 873787781 51035659 348819169 120900720 44828134 245645197 888235023 52696195 901686801 5451175 862058560 693535258 498823868 104075235 579259496 70977421 857069240 235391182 554718100 920595073 969198923 455814944 600573537 459274037 755491119 261410900 928938185 250940183 686751551 656198679 48165539 64362701 998114775 320256708 753450552 325339683 490686919 637843153 138990294 133620478 284457562 579646312 129742992 687543417 725683590 4465817 688037252 790138916 618866742 30030373 854800544 114628225 849703372 991299232 588058798 784474492 260678111 143350275 604398569
# 74 32
# 995277112 872294901 937026685 902889922 544447930 901518221 319610762 634454365 811183778 132544268 169443846 279403800 540414258 827069621 690451694 567476317 392562070 513925484 159359932 243247893 251452341 59161538 628997761 296353524 799100475 118954987 116674799 886734238 598806464 31870606 718825517 350444775 525173351 223699665 269382336 613393276 379284132 689920806 27754867 58055426 218442553 314435548 553978547 375829684 613071739 63157645 426596475 152036570 920575707 289209492 988438883 906297036 825754459 415865499 185149286 100245299 195561045 937481983 965148820 312231949 25312153 219593365 328780009 123166110 671553640 775462495 912878400 124094632 244837365 195904481 267159894 561011159 461338983 101300189 183701608 184419848 725482715 923326986 432799058 319633995 24931396 848618563 86267192 927191375 957075571 709584345 800373202 827819784 768044422 791377015 307265234 301595381 852161547 710678586 70950288 608066331 43632691 481187519 42700878 75604 709149937 148750309 375478255 356076899 340495882 817853166 408315093 341515886 426686149 866208910 581507357 196071602 135500316 814123770 5382284 265734014 573071185 936228078 572625377 240489032 127915748 41824567 511323578 378798730 328725402 205386261 920667898 45685051 969968756 509496293 879874440 270298416 770542885 980855363 944590147 172976936 677988961 205215123 984813757 108346470 705967212 343782409 219937633 465419922 970165258 517138113 673945782 178003796
# 80 94
# 768564869 948595156 120191564 424987968 35146832 947781077 470351340 100645351 122278999 1286014 139200828 938624613 48999829 53889202 270697558 243492960 75326116 138163529 477588074 321865810 87361877 559735838 147350337 468468968 882895274 856352995 82363349 94316553 921331941 114332448 735073118 693451613 447507422 769509760 4014086 685728923 294253990 19454536 140829364 978098910 714041163 751207105 481453022 62558858 307223023 739638751 118634152 19368248 45092017 385759484 999495873 910050677 843194405 323778282 18024076 135451105 194055915 617587259 793574640 381021541 32804233 584930399 538058605 97336718 703164059 268808750 356046540 184757238 746524082 230780400 163694896 86543843 488918860 779825176 222013969 2660722 207555223 660168811 202181006 737038288 716830520 387289970 159591733 51181428 212801596 789130295 846842771 512323528 5089204 782389395 369169762 348912329 184652124 334378153 76396919 393753883 69890105 116923473 771230862 658782920 886336155 350676424 123530800 358447529 735990068 279266156 374515197 995325200 680509917 625249675 933802954 615755602 280707921 983939435 91497076 193065080 144492590 268912529 100260193 884358012 670786797 772034076 273498736 871229950 11242982 568194694 581422427 916136739 52423383 611502811 818493582 434368570 135639837 11569570 614708269 5535013 123640179 403801804 441573886 621796548 879155934 286291378 128799344 653015588 237046277 454612354 70501299 90316305 468178284 292336580 5799371 271737791 546819815 111083770 260106656 483345747 454311806 314158357 190196704 180337392