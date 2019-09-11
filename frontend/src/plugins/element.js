import Vue from 'vue'
import {
  Button,
  Select,
  Option,
  Icon,
  // Dropdown,
  // DropdownMenu,
  // DropdownItem,
  Input,
  Loading,
  Tag,
  Dialog,
  Progress,
  Switch,
  Tooltip
} from 'element-ui'

import { Popup } from 'vant'

Vue.use(Button)
Vue.use(Select)
Vue.use(Option)
Vue.use(Icon)
Vue.use(Input)
Vue.use(Tag)
// Vue.use(Dropdown)
// Vue.use(DropdownMenu)
// Vue.use(DropdownItem)
Vue.use(Tooltip)
Vue.use(Dialog)
Vue.use(Progress)
Vue.use(Switch)

Vue.use(Popup)

// Vue.prototype.$confirm = MessageBox.confirm
Vue.prototype.$loading = Loading.service
