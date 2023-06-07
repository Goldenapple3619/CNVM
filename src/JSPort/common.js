module.exports = {
    get_device: function (motherboard, id) {
        let item = undefined;

        motherboard.connected_dev.forEach(element => {
            if (element.id == id) {
                item = element;
            }
        });
        return (item);
    }
}
