import React from 'react';
import styles from '../../../styles/Map.module.css';

export default class Suffolk extends React.Component {
    render() {
        return (
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 319 147">
                <title>Suffolk</title>
                <g id="Layer_2" data-name="Layer 2">
                    <g id="Layer_2-2" data-name="Layer 2">
                        <path d="M18,143l-7-20V104L8,95,4,90,1,82l5-2h7l-1,7,4,5,5-2h5l4,2V85l15,2,12,6V85h9l6-5-6-6H93s17,3,19,3,26-3,26-3h31l23-19h7l8-10h5l7-7,8-6,15-3,3,2-8,9-4-5-8,3-4,6-8,7-4,3,7,2-1,4-7-1-5,3,3,6-7-2,1,4,4,4-7-1-4-3-7,5-3,6-11,3v5h8l4-3,7,4,9-1,7-6,11-12,1-6,5,3h11l9-4,1-6,4-1,5,9,4-3V56h7l2,9,13-1,7-5,9-4,4-1,3-4,2,3,2-6,11,3s-2,4-2,5-16,7-16,7L211,99s-1-5-2-5h-9l-4,6-7-2-8,4-2,9-11,3s0-5-4-4-7,2-7,2l-7-2-3,5-9,2-6-1-2,8-5,4-4-4-3-5-4,2s-1,5-2,5-5,2-5,2l-6-4-9,1-1,5-9,2s-15-6-14-5,2,8,2,8l-6,2-10-5-11,9-11,2-15,3Z" style={{ fill: `${this.props.color}` }} className={styles.county} onClick={this.props.onClick} />
                        <polygon points="306 1 289 9 284 9 291 1 306 1" style={{ fill: `${this.props.color}` }} className={styles.county} onClick={this.props.onClick} />
                        <polygon points="255 29 260 23 251 23 255 29" style={{ fill: `${this.props.color}` }} className={styles.county} onClick={this.props.onClick} />
                        <polygon points="264 45 264 41 275 39 277 45 273 55 271 47 264 45" style={{ fill: `${this.props.color}` }} className={styles.county} onClick={this.props.onClick} />
                        <polygon points="239 50 229 42 220 50 223 55 233 55 239 60 239 50" style={{ fill: `${this.props.color}` }} className={styles.county} onClick={this.props.onClick} />
                    </g>
                </g>
            </svg>
        )
    }
}
