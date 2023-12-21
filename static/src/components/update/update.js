/** @odoo-module **/

import { Component,useState,onWillStart,onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class UpdateStudent extends Component {
 static template = "todos.update_student";

  redirectToAnotherPage = (path) => {
    window.location.href = path
  };
   loadData = () =>{
    fetch(`/api/student/${this.props.studentId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((x) => x.json())
      .then((y) => {
         this.state.student.name = y.name
         this.state.student.regi_no =  y.regi_no
         this.state.student.mobile =  y.mobile
         this.state.student.course_ids = y.course_ids
        this.state.student.department_id = y.department_id[0];
        console.log(y, this.state.student, y.department_id )
        this.loadCourse()

      });
  };

  updateStudent = () => {
  this.state.student.department_id = parseInt(this.state.student.department_id)
    console.log(this.state.student)
    fetch(`/api/student/${this.props.studentId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(this.state.student),
    })
      .then((x) => x.json())
      .then((y) => {
        this.redirectToAnotherPage("/students")
      });
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
    fetch(`/api/course/${this.state.student.department_id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((x) => x.json())
      .then((y) => (this.state.courses = y));
  };
  onDeptChange = ()=>{
      this.state.student.course_ids = [];
      this.loadCourse()
  }
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
//            name : "",
//            regi_no : "",
//            mobile : "",
//            department_id : "",
//            course_ids : [],
        },
          department: [],
          courses: [],
    });

    onWillStart(() => {
        console.log("CALLED APP")
          this.loadData();
          this.loadDept();
    });
  }
}


