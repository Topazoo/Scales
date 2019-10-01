// WebSocket client library

angular.module('Sockets_Library', ['ngWebSocket'])
.controller('Weight_Socket', ['$scope', '$websocket', function($scope, $websocket) {
    $websocket('ws://localhost:5001').onMessage(function(message) {
        data = JSON.parse(message.data);
        $scope.weight = data.weight;
    });
}]);