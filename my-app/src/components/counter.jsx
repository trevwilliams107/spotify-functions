import React, { Component } from "react";

class Counter extends Component {
  styles = {
    fontSize: 50,
    fontWeight: "bold",
  };

  render() {
    return (
      <div>
        <h3>Counter {this.props.counter.id}</h3>
        <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
        <button
          onClick={() => this.props.onIncrement(this.props.counter)}
          className="btn btn-primary m-2"
        >
          Increment
        </button>
        <button
          className="btn btn-danger btn-sm m-2"
          onClick={() => this.props.onDelete(this.props.counter.id)}
        >
          Delete
        </button>
        <h6></h6>
      </div>
    );
  }
  // <ul>
  // {this.state.tags.map((tag) => (
  //   <li key={tag.id}>{tag.name}</li>
  // ))}
  // </ul>

  getBadgeClasses() {
    let classes = "badge m-2 badge-";
    classes += this.props.counter.value === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    return this.props.counter.value === 0 ? "Zero" : this.props.counter.value;
  }
}
export default Counter;
