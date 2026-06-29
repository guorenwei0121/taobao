# taobao
selenium爬取淘宝方便面前20页商品数据  
初始化和搜索：  
使用webdriver.Chrome()初始化 Chrome 浏览器驱动，并打开淘宝首页。  
通过driver.find_element(By.ID, 'q')定位搜索框，输入 “方便面”，并随机等待一段时间模拟用户输入速度。  
定位搜索按钮并点击，之后再随机等待页面加载。  
页面爬取：  
在每一页爬取时，通过driver.execute_script(f"window.scrollTo(0, {scroll_height});")随机滚动页面到一定高度，模拟用户浏览行为。  
定位每个商品元素，使用ActionChains模拟鼠标悬停操作，等待一段时间后获取商品标题、价格和发货地址信息。  
将每个商品信息以字典形式添加到product_list列表中。  
翻页操作：  
查找下一页按钮，若按钮可用且不是最后一页，随机等待后点击进入下一页，并再次随机等待页面加载。  
数据存储：   
爬取结束后，使用pandas将数据转换为DataFrame并保存为 Excel 文件。
