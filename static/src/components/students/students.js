/** @odoo-module **/

import { Component,useState,onWillStart,onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class Student extends Component {
 static template = "todos.student_sec";
    deleteStudent = (id) => {
    fetch(`/api/student/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },

    })
      .then((y) => this.loadData());
  };
  loadData = () =>{
    fetch("/api/student", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((x) => x.json())
      .then((y) => (this.state.students = y));
  };


  setup() {
  onMounted(() => console.log("props",this.props));
    this.state = useState({
          students: [],
    });

    onWillStart(() => {
    console.log("CALLED APP")
      this.loadData();
    });
  }
}


