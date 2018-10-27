import React, {Component} from 'react';


export default class Details extends Component{
    render(){
        return(
            <table className="table table-hover">
                <tbody>
                    <tr>
                        <th scope="row">Cost of path</th>
                        <td>{this.props.costOfPath}</td>
                    </tr>
                    <tr>
                        <th scope="row">Number of nodes expanded</th>
                        <td>{this.props.expandedNodes}</td>
                    </tr>
                    <tr>
                        <th scope="row">Search depth</th>
                        <td>{this.props.depth}</td>
                    </tr>
                    <tr>
                        <th scope="row">Running time (in seconds)</th>
                        <td>{this.props.runningTime}</td>
                    </tr>
                </tbody>
            </table>
        );
    }
}
