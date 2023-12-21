/** @odoo-module **/

import { Component,useState,onWillStart,onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class ToDo extends Component {
 static template = "todos.test_todo";
  toggleTask = (task) => {
    task.is_completed = !task.is_completed;
    fetch(`/api/todos/${task.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(task),
    })
      .then((y) => this.loadData());
  };
  deleteTask = (taskId) => {
    fetch(`/api/todos/${taskId}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },

    })
      .then((y) => this.loadData());
  };
  addTask = () => {
    fetch(`/api/todos`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(this.state.task),
    })
      .then((x) => x.json())
//      .then((y) => console.log(y) );
      .then((y) => this.loadData() );

    this.state.task.name = "";
  };
  loadData = () => {
    fetch("/api/todos", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((x) => x.json())
      .then((y) => (this.state.tasks = y));
  };
  setup() {
  onMounted(() => console.log("props",this.props));
    this.state = useState({
      task: {
        name: "",
        is_completed: false,
      },
      tasks: [],
    });

    onWillStart(() => {
      this.loadData();
    });
  }
}

////ToDo.components = {};
//ToDo.template = "todos.clientaction";
//
//registry.category("actions").add("todos.dashboard", ToDo);
