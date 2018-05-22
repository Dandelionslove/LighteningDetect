<template>
  <div class="layout background-size">
    <Layout class="main-size">
      <Header>
        <Menu mode="horizontal" active-name="1" @on-select="dealSelect">
          <div class="demo-avatar user-div">
            <Avatar class="user-avatar">Y</Avatar>
            <span class="greeting">Hello, Ygritte</span>
          </div>
          <div class="layout-nav">
            <MenuItem name="logout">
              <Icon type="person"></Icon>
              Logout
            </MenuItem>
          </div>
        </Menu>
      </Header>
      <Layout class="main-size">
        <Sider hide-trigger :style="{background: '#fff'}" class="sider-bar">
          <Menu active-name="1-2" theme="light" width="auto" :open-names="['1']">
            <Submenu name="1">
              <template slot="title">
                <Icon type="ios-navigate"></Icon>
                Item 1
              </template>
              <MenuItem name="1-1">Option 1</MenuItem>
              <MenuItem name="1-2">Option 2</MenuItem>
            </Submenu>
            <Submenu name="2">
              <template slot="title">
                <Icon type="ios-keypad"></Icon>
                Item 2
              </template>
              <MenuItem name="2-1">Option 1</MenuItem>
              <MenuItem name="2-2">Option 2</MenuItem>
            </Submenu>
            <Submenu name="3">
              <template slot="title">
                <Icon type="ios-analytics"></Icon>
                Item 3
              </template>
              <MenuItem name="3-1">Option 1</MenuItem>
              <MenuItem name="3-2">Option 2</MenuItem>
            </Submenu>
          </Menu>
        </Sider>
        <Layout :style="{padding: '0 24px 24px'}">
          <i-input class="dashboard-search">
            <i-button slot="append" icon="ios-search"></i-button>
          </i-input>
          <graph></graph>
        </Layout>
      </Layout>
    </Layout>
  </div>
</template>

<script>
  import graph from "./Graph.vue"
  import Graph from "./Graph";
  import { logout, isLogin } from '../service/apis'

  export default {
    components: {Graph},
    name: "dashboard",
    methods: {
      dealSelect (name) {
        switch (name) {
          case 'logout':
            this.userLogout()
                break
        }
      },
      userLogout () {
        logout().then(res => {
          console.log(res)
          res = JSON.parse(res)
          if (res.status === 'OK') {
            this.$session.remove('username')
            this.$router.push({name: 'Login'})
          }
        }).catch(err => {
          console.error(err)
        })
      }
    },
    created () {
      console.log(this.$session.get('groups'))
      // isLogin(this.$session.get('username')).then(res => {
      //   console.log(res)
      //   res = JSON.parse(res)
      //   if (res.status === 'FAIL') {
      //     this.$router.push({name: 'Login'})
      //   }
      // }).catch(err => {})
    }
  }
</script>

<style scoped>
  .layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
    height: 100%;
  }

  .layout-nav{
    margin: 0 auto;
    margin-right: 20px;
    float: right;
  }
  .ivu-layout-header{
    background: #ffffff;
  }
  .mybread{
    float: left;
  }
  .ivu-menu-horizontal {
    height: 64px;
    line-height: 64px;
  }
  .user-avatar{
    color: #f56a00;
    background-color: #fde3cf;
  }
  .user-div{
    float: left;
    top:50%;
  }
  .greeting{
    margin-left: 10px;
  }
  .background-size{
    position:absolute;
    width: 100%;
    height: 100%;
  }
  .main-size{
    height: 100%;
  }
  .dashboard-search{
    margin-top: 10px;
    margin-bottom: 10px;
    width: 200px;
    align-self: flex-end;
  }
</style>
