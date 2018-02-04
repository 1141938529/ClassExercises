import re

str = '''
<script type="text/javascript">
            var $PAGE = {};
            $PAGE.isCate2 = "0";
            $PAGE.cateid = "0";
            $PAGE.pager = {
                count: "56",
                current: "1"
            };
            $PAGE.emperorIcon = "";
            $PAGE.cate2_id = "null";
            $PAGE.cate1_id = "null";
            $PAGE.rk= "0_0";
            $PAGE.ivcv = 0;
        </script>
'''
reStockName = '<script>'
