<template>
<div class="main_content">
  <div class="block">
    <el-carousel :interval="4000" type="card" height="300px" trigger="click">
        <el-carousel-item v-for="item in 6" :key="item">
            <div :class="'img'+item"></div>
        </el-carousel-item>
    </el-carousel>
  </div>
  <div class="serach">
    <el-button type="text" style="float: left;font-size: 15px" @click="show_all">全部</el-button>
    <el-button type="text" style="float: left;font-size: 15px" @click="lianzai_all">正连载</el-button>
    <el-button type="text" style="float: left;font-size: 15px" @click="finall_all">已完结</el-button>
    <el-button type="primary" plain class="ser_bt" @click="serach" icon="el-icon-search">搜索</el-button>
    <el-input v-model="ser_data" placeholder="请输入内容" class="ser_in"></el-input>
  </div>
  <div class="box_body">
      <div class="lis" v-for="item in feiye" :key="item.id">
          <a :href="'#/cartoon/book/'+item.id" target="_blank">
            <img :src="item.image">
          </a>
          <a :href="'#/cartoon/book/'+item.id" class="cartoon_name" target="_blank">{{ item.title }}</a>
          <p style="font-size: 13px">{{ item.describe }}</p>
      </div>
  </div>
  <el-pagination
  background
  @current-change="handleCurrentChange"
  :current-page="currentPage"
  :page-size="pagesize" 
  layout="total,prev,pager,next,jumper"
  :total="arr.length">
  </el-pagination>
  <br>
  <br>
</div>
  
</template>

<script>
import {AllCartoon, TypeCartoon} from '@/api/manhua'
export default {
    data() {
        return {
            // 全部漫画
            arr: [],
            all_arr: [],
            // 连载漫画
            lianzai_arr: [],
            // 完结漫画
            wanjie_arr: [],
            currentPage: 1, //初始页
            pagesize: 48, //    每页的数据
            p:1,
            search_result: [],
            ser_data: ''
        }
    },
    computed: {
        feiye() {
            return this.arr.slice((this.currentPage-1)*this.pagesize,this.currentPage*this.pagesize)
        }
    },
    methods: {
        async get_res() {
            let all_data = await AllCartoon()
            if(all_data.state == 'OK'){
                this.arr = all_data.arr
                this.all_arr = all_data.arr
            }
            let type_data = await TypeCartoon()
            if(type_data.state == 'OK'){
                this.lianzai_arr = type_data.lianzai_arr
                this.wanjie_arr = type_data.wanjie_arr
            }
        },

        handleCurrentChange(val) {
            this.currentPage = val;
            sessionStorage.setItem('currentPage', val)
            window.scrollTo(0,0);
            // this.arry = this.arr.slice((this.currentPage-1)*this.pagesize,this.currentPage*this.pagesize)
        },
        // 搜索方法
        serach() {
            this.search_result = []
            for(let i=0;i<this.all_arr.length;i++){
                if(this.all_arr[i].title.indexOf(this.ser_data) != -1){
                    this.search_result.push(this.all_arr[i])
                }
            }
            this.currentPage = 1
            this.arr = this.search_result
        },
        show_all() {
            this.arr = this.all_arr
        },
        // 展示正连载的方法
        lianzai_all() {
            this.arr = this.lianzai_arr
        },
        // 展示已完结的方法
        finall_all() {
            this.arr = this.wanjie_arr
        }
    },
    async mounted() {
        if(sessionStorage.getItem('currentPage')){
            this.currentPage = parseInt(sessionStorage.getItem('currentPage'))
        }
        this.get_res()
        this.arr = this.arr.slice((this.currentPage-1)*this.pagesize,this.currentPage*this.pagesize)
    }
}
</script>

<style scoped>
    .main_content{
        width: 100%;
        height: 100%;
        background-image: url('../../assets/registerbck.png');
        background-size: cover;
    }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .block{
      width: 80%;
      margin-left: auto;
      margin-right: auto;
      padding-top: 10px;
  }
  .box_body{
      width: 80%;
      min-height: 200px;
      margin-right: auto;
      margin-left: auto;
      /* background-color: white; */
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      align-content: flex-start;
  }
  .img1{
      height: 350px;
      background-image: url('http://www.qiruiyaoye.cn/upload/book/1.jpg');
      background-size: 100% 100%;
  }
  .img2{
      height: 350px;
      background-image: url('http://www.qiruiyaoye.cn/upload/book/4577.jpg');
      background-size: 100% 100%;
  }
  .img3{
      height: 350px;
      background-image: url('http://www.qiruiyaoye.cn/upload/book/4562.jpg');
      background-size: 100% 100%;
  }
  .img4{
      height: 350px;
      background-image: url('http://www.qiruiyaoye.cn/upload/book/4579.jpg');
      background-size: 100% 100%;
  }
  .img5{
      height: 350px;
      background-image: url('http://www.qiruiyaoye.cn/upload/book/14.jpg');
      background-size: 100% 100%;
  }
  .img6{
      height: 350px;
      background-image: url('http://www.qiruiyaoye.cn/upload/book/18.jpg');
      background-size: 100% 100%;
  }
  .lis{
      width: 180px;
      height: 280px;
      margin: 10px;
      /* background-color: #E4E7ED; */
  }
  .lis:hover{
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
  }
  .lis img{
      width: 180px;
      height: 220px;
  }
  .cartoon_name{
      text-decoration: none;
      color: black;
      font-weight: bold;
      font-size: 15px;
      margin-bottom: 5px;
  }
  .cartoon_name:hover{
      color: #9ad2c9;
  }

  .serach{
    width: 80%;
    margin-right: auto;
    margin-left: auto;
    height: 40px;
    text-align: center;
    margin-bottom: 20px;
  }
  .ser_in{
    float: right;
    width: 250px;
  }
  .ser_bt{
    float: right;
  }

</style>
