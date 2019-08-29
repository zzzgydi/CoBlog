import Vue from 'vue'
import {
  Button,
  Row,
  Col,
  Select,
  Option,
  Icon,
  Dropdown,
  DropdownMenu,
  DropdownItem,
  Form,
  FormItem,
  Input,
  Message,
  MessageBox,
  Tag,
  Dialog
} from 'element-ui'

Vue.use(Button)
Vue.use(Row)
Vue.use(Col)
Vue.use(Select)
Vue.use(Option)
Vue.use(Icon)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Tag)
Vue.use(Dropdown)
Vue.use(DropdownMenu)
Vue.use(DropdownItem)
Vue.use(Dialog)

Vue.prototype.$message = Message
Vue.prototype.$confirm = MessageBox.confirm
