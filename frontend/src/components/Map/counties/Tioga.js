import React from 'react';
import styles from '../../../styles/Map.module.css';

export default class Tioga extends React.Component {
    render() {
        return (
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 100">
                <title>Tioga</title>
                <g id="Layer_2" data-name="Layer 2">
                    <g id="Layer_2-2" data-name="Layer 2">
                        <polygon points="92 99 1 99 4 81 4 72 8 59 8 34 20 34 22 38 30 38 31 23 43 23 45 27 55 27 59 30 63 20 66 14 51 7 55 4 62 1 89 1 89 18 95 33 95 54 89 56 92 99" style={{ fill: `${this.props.color}` }} className={styles.county} onClick={this.props.onClick} />
                    </g>
                </g>
            </svg>
        )
    }
}
