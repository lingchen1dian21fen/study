package com.cbo.elastic;

import com.cbo.util.poi.ExcelBean;
import com.cbo.util.poi.ExcelReader;
import org.elasticsearch.action.bulk.BulkRequestBuilder;
import org.elasticsearch.action.bulk.BulkResponse;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.action.update.UpdateRequestBuilder;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;
import org.elasticsearch.common.xcontent.XContentBuilder;
import org.elasticsearch.common.xcontent.XContentFactory;
import org.elasticsearch.transport.client.PreBuiltTransportClient;

import java.io.IOException;
import java.net.InetAddress;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ExecutionException;

/**
 * @Author: chengbo
 * @Date: 2018/10/12
 */
public class DataBuildApp {

    public static final String USER_INDEX = "test";
    public static final String USER_TYPE_MAN = "message";

    public static void main(String[] args) throws IOException, InterruptedException, ExecutionException {
        Settings set = Settings.builder().put("cluster.name", "test_es").build();
        PreBuiltTransportClient client = new PreBuiltTransportClient(set);
        client.addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("192.168.252.129"), 9300));
        BulkRequestBuilder bulkRequestBuilder = client.prepareBulk();
        ExcelReader reader = new ExcelReader("E:/chengbo/personal/phone-num/masage.xlsx");
        ExcelBean excelBean = reader.buildHasHead();
        List<Map<String, Object>> rows = excelBean.getSheetBeans().get(0).getRows();
        for (Map<String,Object> map: rows) {
            UpdateRequestBuilder builder = client.prepareUpdate(USER_INDEX,USER_TYPE_MAN, UUID.randomUUID().toString()).setDocAsUpsert(true).setDoc(map);
            bulkRequestBuilder.add(builder);
        }
        BulkResponse bulkResponse = bulkRequestBuilder.execute().actionGet();
        System.out.println(bulkResponse.status());
    }


}
