/** @odoo-module **/

import { Component,useState,onWillStart,onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class AddStudent extends Component {
 static template = "todos.add_student";

  redirectToAnotherPage = (path) => {
    window.location.href = path
  };
  addStudent = () => {
    console.log("SUBMITTED")
    fetch(`/api/student`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(this.state.student),
    })
      .then((x) => x.json())
      .then((y) => this.redirectToAnotherPage("/students"));
//    this.state.student.name = "";
//    this.state.student.regi_no = "";
//    this.state.student.department_id = "";
//    this.state.student.mobile = "";
//    this.state.student.course_ids = [];
  };

  loadDept = () =>{
    fetch("/api/department", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((x) => x.json())
      .then((y) => (this.state.department = y));
  };
  loadCourse = () =>{
    this.state.student.course_ids = [];
    fetch(`/api/course/${this.state.student.department_id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((x) => x.json())
      .then((y) => (this.state.courses = y));
  };
  onCourseChange = (e,course_id)=>{
       if(e.target.checked){
        this.state.student.course_ids = [...this.state.student.course_ids,course_id]
       }else{
        this.state.student.course_ids = this.state.student.course_ids.filter((id)=> id!=course_id)
       }
       console.log(this.state.student.course_ids)
    }
  setup() {
    onMounted(() => console.log("props",this.props));
    this.state = useState({
        student : {
            name : "",
            regi_no : "",
            mobile : "",
            department_id : "",
            course_ids : [],
        },
          department: [],
          courses: [],
    });

    onWillStart(() => {
        console.log("CALLED APP")
      this.loadDept();
    });
  }
}


