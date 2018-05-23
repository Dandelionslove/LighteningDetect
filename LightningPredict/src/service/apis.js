import fetch from './fetch'

var login = (username, password) => fetch('POST', 'login/', {username: username, password: password})

var logout = () => fetch('GET', 'logout/', {})

var isLogin = (username) => fetch('GET', 'is_login/?username=' + username, {})

var register = (username, password) => fetch('POST', 'register/', {username: username, password: password})


export {
  login,
  logout,
  isLogin,
  register
}
