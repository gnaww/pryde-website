import React from 'react';

export default class Essex extends React.Component {
    render() {
        return (
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 202 190" onClick={this.props.onClick}>
                <defs>
                    <style>{`\
                            .cls-1{\
                                fill: ${this.props.color} ;\
                                stroke:#000;\
                                stroke-linejoin:round;\
                                stroke-width:2px;\
                            }\
                        `}</style>
                </defs>
                <title>Essex</title>
                <g id="Layer_2" data-name="Layer 2">
                    <g id="Layer_2-2" data-name="Layer 2">
                        <polygon class="cls-1" points="1 147 23 173 38 167 42 173 55 177 55 189 173 174 183.37 174 183 168 186 168 186 153 180 147 180 122 173 118 181 95 184 92 182 83 198 70 195 49 193 44 201 30 201 14 193 1 169 5 169 10 162 17 153 16 146 23 38 36 47 98 11 100 15 137 1 147" />
                    </g>
                </g>
            </svg >
        )
    }
}