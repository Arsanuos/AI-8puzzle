import React, {Component} from 'react';
import './cell.css';

export default class Board extends Component{

    constructor(props){
        super(props)

    }

      createTable(){
        let table = []

        // Outer loop to create parent
        for (let i = 0; i < 3; i++) {
          let children = []
          //Inner loop to create children
          for (let j = 0; j < 3; j++) {
                if((this.props.data != undefined && this.props.disabled)){
                    children.push(
                        <td key={j+(this.props.disabled ? 100 : 0)} className="cell">
                            <input key={i*3+(j+1)+ (this.props.disabled ? 100 : 0)} type="text"  data-row={i} data-col={j}  maxLength='1'
                                    disabled = {(this.props.disabled) ? "disabled" : ""}
                                    onKeyUp={this.props.handleBlur} value={this.props.data[3*i + j]}/>
                        </td>)
                }else{
                    children.push(
                        <td key={j+(this.props.disabled ? 100 : 0)} className="cell">
                            <input key={i*3+(j+1)+ (this.props.disabled ? 100 : 0)} type="text"  data-row={i} data-col={j}  maxLength='1'
                            disabled = {(this.props.disabled) ? "disabled" : ""}
                            onKeyUp={this.props.handleBlur} />
                        </td>)
                }
          }
          //Create the parent and add the children
          table.push(<tr key={i}>{children}</tr>)
        }
        return table
      }

    render(){
        return(

        <div>
            <table className="table table-bordered ">
                <tbody>
                    {
                        this.createTable()
                    }
                </tbody>
            </table>
        </div>

        );
    }
}
